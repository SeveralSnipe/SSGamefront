from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import CustomUserCreationForm, HomeForm, OrganizationProfileForm, TempForm
from .models import Area, OrganizationLocationAmenities, OrganizationLocationGameType, OrganizationLocation, Organization, OrganizationLocationWorkingDays, GameType, Tenant
# Create your views here.
class HomeForm(FormView):
    form_class=TempForm
    template_name='home.html'
    success_url='locationsdisplay'
    def form_valid(self, form):
            org_and_desc_obj=[]
            form=form.cleaned_data
            #day=form['date'].strftime('%A')
            game=form['game']
            area_from_form=form['area']
            areaobj=OrganizationLocation.objects.filter(area=area_from_form)
            for location in areaobj:
                # workingdaysobj=OrganizationLocationWorkingDays.objects.get(organization=location)
                # if workingdaysobj.check_working(day):
                org_and_desc_obj += list(OrganizationLocationGameType.objects.filter(game_type=game,organization_location=location).values('organization_location','description'))
            objlist=[]
            for result in org_and_desc_obj:
                name_desc_pair={}
                name_desc_pair['name']=OrganizationLocation.objects.get(pk=result['organization_location']).organization.organization_name
                name_desc_pair['desc']=result['description']
                objlist.append(name_desc_pair)
            self.request.session['area']=area_from_form.area_name
            self.request.session['game']=game.game_name
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
    areaobj=Area.objects.get(area_name=area)
    gameobj=GameType.objects.get(game_name=game_name)
    organizationobj=Organization.objects.get(organization_name=org)
    locationobj=OrganizationLocation.objects.get(organization=organizationobj,area=areaobj)
    locationgame=OrganizationLocationGameType.objects.get(organization_location=locationobj,game_type=gameobj)
    amenitiesobj=OrganizationLocationAmenities.objects.get(organization_location=locationobj)
    workinglist=[]
    #workingobj=OrganizationLocationWorkingDays.objects.filter(organization=locationobj)
    for i in range(7):
        daytimeobj=OrganizationLocationWorkingDays.objects.get(organization_location=locationobj, days=i)
        startendpair={}
        startendpair['start']=daytimeobj.work_from_time
        startendpair['end']=daytimeobj.work_to_time
        workinglist.append(startendpair)
    #workingobj=OrganizationLocationWorkingDays.objects.get(organization=locationobj)
    print(workinglist)
    context_dict={'org':org,
                  'area':area,
                  'game':game_name,
                  'pricing':locationgame.pricing,
                  'contact':locationobj.phone_number,
                  'address':locationobj.address_line_1+' '+locationobj.address_line_2,
                  'parking':('No','Yes') [amenitiesobj.is_parking],
                  'restrooms':('No','Yes')[amenitiesobj.is_restrooms],
                  'changerooms':('No','Yes')[amenitiesobj.is_changerooms],
                  'powerbackup':('No','Yes')[amenitiesobj.is_powerbackup],
                  'beverages':('No','Yes')[amenitiesobj.is_powerbackup],
                  'coaching':('No','Yes')[amenitiesobj.is_coaching_facilities],
                  'description':amenitiesobj.description,
                #   'monday':('No','Yes')[workingobj.is_monday_workingday],
                #   'tuesday':('No','Yes')[workingobj.is_tuesday_workingday],
                #   'wednesday':('No','Yes')[workingobj.is_wednesday_workingday],
                #   'thursday':('No','Yes')[workingobj.is_thursday_workingday],
                #   'friday':('No','Yes')[workingobj.is_friday_workingday],
                #   'saturday':('No','Yes')[workingobj.is_saturday_workingday],
                #   'sunday':('No','Yes')[workingobj.is_sunday_workingday],
                  'sunday':workinglist[0],
                  'monday':workinglist[1],
                  'tuesday':workinglist[2],
                  'wednesday':workinglist[3],
                  'thursday':workinglist[4],
                  'friday':workinglist[5],
                  'saturday':workinglist[6],
                }
    return render(request, 'locationdetail.html', context=context_dict)
class CreateUserProfileView(CreateView):
    model = Organization
    form_class = OrganizationProfileForm
    user_form_class = CustomUserCreationForm
    template_name = 'neworg.html'
    success_url = reverse_lazy('placeholder')

    def get(self, request):
        profile_form = self.form_class()
        user_form = self.user_form_class()
        return render(request, self.template_name, {'profile_form': profile_form, 'user_form': user_form})

    def post(self, request):
        profile_form = self.form_class(request.POST)
        user_form = self.user_form_class(request.POST)
        if all([profile_form.is_valid(), user_form.is_valid()]):
            random_password=user_form.generate_temp_password()
            user = user_form.save(random_password, commit=False)
            user.groups.add(Group.objects.get(name="Organization"))
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.tenant=Tenant.objects.get(id=1)
            profile.save()
            current_site = get_current_site(self.request)
            subject = 'Welcome to Our Website'
            message = render_to_string('registration/signup_email.html', {'user': user,'domain': current_site.domain, 'temppwd': random_password})
            from_email = 'testgamefront@gmail.com'
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        else:
            return render(request, self.template_name, {'profile_form': profile_form, 'user_form': user_form})

        return HttpResponseRedirect(self.success_url)

class MyLoginView(LoginView):
    #redirect_authenticated_user = True
    template_name='login.html'
    
    def get_success_url(self):
        return reverse_lazy('home') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

