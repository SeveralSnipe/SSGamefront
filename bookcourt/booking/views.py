import datetime
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from common.forms import BookingForm
from common.models import *

# Create your views here.
class BookingView(FormView):
    form_class=BookingForm
    success_url=reverse_lazy('placeholder')
    template_name='booking.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        gametype=OrganizationLocationGameType.objects.get(pk=self.request.session.get('gametypepk'))
        date=self.request.session.get('date')
        date=datetime.datetime.strptime(date,'%d-%m-%Y')
        day=date.strftime('%A')
        workingtime=OrganizationLocationWorkingTime.objects.get(organization_location=gametype.organization_location, work_day_choices=day)
        fromtime=workingtime.from_time
        delta=datetime.timedelta(hours=fromtime.hour,minutes=fromtime.minute).total_seconds()
        from_minutes=delta//60
        totime=workingtime.to_time
        delta=datetime.timedelta(hours=totime.hour,minutes=totime.minute).total_seconds()
        to_minutes=delta//60
        context['organizationname']=gametype.organization_location.organization.organization_name
        context['gamename']=gametype.game_type
        context['date']=date
        context['from_minutes']=from_minutes
        context['to_minutes']=to_minutes
        context['pricing']=gametype.pricing
        self.request.session['pricing']=str(gametype.pricing)
        return context
        
    def form_valid(self, form):
        form=form.cleaned_data
        self.request.session['starttime']=form['start_time'].strftime('%H:%M')
        print(form)
        total_minutes=form['hours']*60+form['minutes']
        print(total_minutes)
        price_per_half_hour=float(self.request.session.get('pricing'))
        print(price_per_half_hour)
        price=price_per_half_hour*(total_minutes//30)
        print(price)
        self.request.session['hours']=form['hours']
        self.request.session['minutes']=form['minutes']
        self.request.session['totalprice']=price
        return super().form_valid(form)
