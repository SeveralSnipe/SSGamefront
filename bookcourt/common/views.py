from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView
from .forms import HomeForm
from .models import OrganizationLocationAmenities, OrganizationLocationGameType, OrganizationLocation, Organization, OrganizationLocationWorkingDays, GameType
# Create your views here.
class HomeForm(FormView):
    form_class=HomeForm
    template_name='home.html'
    success_url='locationsdisplay'
    def form_valid(self, form):
            org_and_desc_obj=[]
            form=form.cleaned_data
            day=form['date'].strftime('%A')
            game=form['game']
            location_from_form=form['location']
            areaobj=OrganizationLocation.objects.filter(area=location_from_form.area)
            for location in areaobj:
                workingdaysobj=OrganizationLocationWorkingDays.objects.get(organization=location)
                if workingdaysobj.check_working(day):
                    org_and_desc_obj += list(OrganizationLocationGameType.objects.filter(game_type=game,organization_location=location).values('organization_location','description'))
            objlist=[]
            for result in org_and_desc_obj:
                name_desc_pair={}
                name_desc_pair['name']=OrganizationLocation.objects.get(pk=result['organization_location']).organization.organization_name
                name_desc_pair['desc']=result['description']
                objlist.append(name_desc_pair)
            self.request.session['area']=location_from_form.area
            self.request.session['game']=game.name
            self.request.session['objlist']=objlist
            #response=render(self.request,'locationsdisplay.html',{'objlist':objlist})
            return super().form_valid(form)
    
def locationsdisplay(request):
     objlist=request.session.get('objlist')
     game=request.session.get('game')
     area=request.session.get('area')
     return render(request,'locationsdisplay.html',{'objlist':objlist,'game':game,'area':area})

def locationdetail(request):
    org=request.GET['orgname']
    area=request.session.get('area')
    game_name=request.session.get('game')
    gameobj=GameType.objects.get(name=game_name)
    organizationobj=Organization.objects.get(organization_name=org)
    locationobj=OrganizationLocation.objects.get(organization=organizationobj,area=area)
    locationgame=OrganizationLocationGameType.objects.get(organization_location=locationobj,game_type=gameobj)
    amenitiesobj=OrganizationLocationAmenities.objects.get(organization_location=locationobj)
    workingobj=OrganizationLocationWorkingDays.objects.get(organization=locationobj)
    context_dict={'org':org,
                  'area':area,
                  'game':game_name,
                  'pricing':locationgame.pricing,
                  'contact':locationobj.contact_number,
                  'address':locationobj.address_line_1+' '+locationobj.address_line_2,
                  'parking':('No','Yes') [amenitiesobj.is_parking],
                  'restrooms':('No','Yes')[amenitiesobj.is_restrooms],
                  'changerooms':('No','Yes')[amenitiesobj.is_changerooms],
                  'powerbackup':('No','Yes')[amenitiesobj.is_powerbackup],
                  'beverages':('No','Yes')[amenitiesobj.is_powerbackup],
                  'coaching':('No','Yes')[amenitiesobj.is_coaching_facilities],
                  'description':amenitiesobj.description,
                  'monday':('No','Yes')[workingobj.is_monday_workingday],
                  'tuesday':('No','Yes')[workingobj.is_tuesday_workingday],
                  'wednesday':('No','Yes')[workingobj.is_wednesday_workingday],
                  'thursday':('No','Yes')[workingobj.is_thursday_workingday],
                  'friday':('No','Yes')[workingobj.is_friday_workingday],
                  'saturday':('No','Yes')[workingobj.is_saturday_workingday],
                  'sunday':('No','Yes')[workingobj.is_sunday_workingday],
                }
    return render(request, 'locationdetail.html', context=context_dict)

