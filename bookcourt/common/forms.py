from django import forms
from .models import *
from django.forms import DateInput, ModelChoiceField, SelectDateWidget, TimeInput, ValidationError, modelformset_factory
from django.contrib.auth.models import User
from smart_selects.form_fields import ChainedModelChoiceField
from durationwidget.widgets import TimeDurationWidget

class HomeFormChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.game_name
class CountryFormChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.country_name

class StateFormChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.state_name

class CityFormChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.city_name

class AreaFormChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.area_name
class HomeForm(forms.Form):
    game=HomeFormChoiceField(queryset=GameType.objects.filter(is_active=True), label='Select Gametype')
    country_name=CountryFormChoiceField(queryset=Country.objects.filter(is_active=True), label='Select Country')
    state_name=ChainedModelChoiceField('common','State','country_name','country_name','common','Country','country_name',show_all=False,auto_choose=False)
    city_name=ChainedModelChoiceField('common','City','state_name','state_name','common','State','state_name',show_all=False,auto_choose=False)
    area_name=ChainedModelChoiceField('common','Area','city_name','city_name','common','City','city_name',show_all=False,auto_choose=False)
    #date=forms.DateField(widget=SelectDateWidget(),label='Select Date')
# class SearchForm(forms.ModelForm):
#     game=HomeFormChoiceField(queryset=GameType.objects.filter(is_active=True), label='Select Gametype')
#     #date=forms.DateField(widget=SelectDateWidget(),label='Select Date')
#     class Meta:
#         model=OrganizationLocation
#         fields=['country_name','state_name','city_name','area_name']

class TempForm(forms.Form):
    game=HomeFormChoiceField(queryset=GameType.objects.filter(is_active=True), label='Select Gametype')
    area=AreaFormChoiceField(queryset=Area.objects.filter(is_active=True), label='Select Area')
    date=forms.DateField(widget=DateInput(attrs={'type':'date'}))



class CustomUserCreationForm(forms.Form):  
    first_name= forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)  
    email = forms.EmailField(label='Organization Email')  
  
    def generate_temp_password(request):
        password = User.objects.make_random_password(length=6, allowed_chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        return password
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email    
  
    def save(self, pwd, commit = True,): 
        user = User.objects.create_user(  
            self.cleaned_data['email'],  
            self.cleaned_data['email'],  
            pwd,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        return user

class OrganizationSignupForm(forms.ModelForm):
    class Meta:
        model= Organization
        fields=["organization_name","phone_number"]
class TimeForm(forms.ModelForm):
    class Meta:
        model=OrganizationLocationWorkingTime
        fields=['is_active','from_time','to_time']
        widgets={
            #'work_day_choices':forms.TextInput(attrs={'readonly': True}),
            'from_time': forms.TimeInput(attrs={'type':'time', 'required': False}),
            'to_time': forms.TimeInput(attrs={'type':'time', 'required': False}),
        }
        labels={
            'is_active':'Working',
            #'work_day_choices':'Day',
            'from_time':'From',
            'to_time':'To',
        }
        required={
            'is_active',
            #'work_day_choices',
        }
        
    def clean(self):
        from_time=self.cleaned_data.get('from_time')
        to_time=self.cleaned_data.get('to_time')
        is_active=self.cleaned_data.get('is_active')
        if(is_active):
            if(from_time==None or to_time==None):
                raise ValidationError("You must enter timings for active days.")
        return
    
TimeModelFormset=modelformset_factory(OrganizationLocationWorkingTime, TimeForm, extra=0)
class OrganizationProfileForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields=['organization_name','phone_number','alt_number','description']

class LocationForm(forms.ModelForm):
    class Meta:
        model = OrganizationLocation
        fields=['address_line_1','address_line_2','area','pincode','phone_number']
        widgets = {
          'address_line_1': forms.Textarea(attrs={'rows':1, 'cols':25}),
          'address_line_2': forms.Textarea(attrs={'rows':1, 'cols':25}),
        }

class AmenitiesForm(forms.ModelForm):
    class Meta:
        model = OrganizationLocationAmenities
        exclude = ('organization_location','is_active',)
        widgets = {
          'description': forms.Textarea(attrs={'rows':5, 'cols':35}),
        }

class GameTypeForm(forms.ModelForm):
    
    class Meta:
        model = OrganizationLocationGameType
        exclude = ('organization_location','is_active',)
        widgets = {
          'description': forms.Textarea(attrs={'rows':5, 'cols':35}),
        }
    
class TermsForm(forms.Form):
    agree=forms.BooleanField()
    
class TestForm(forms.Form):
    duration=forms.DurationField(widget=TimeDurationWidget(show_days=False, show_seconds=False))

class TestJSForm(forms.Form):
    hours=forms.IntegerField(disabled=True, min_value=0, initial=0)
    minutes=forms.IntegerField(disabled=True, min_value=0, initial=0)

class BookingForm(forms.Form):
    start_time=forms.TimeField(widget=TimeInput(attrs={'type':'time'}))
    hours=forms.IntegerField(widget=forms.NumberInput(attrs={'readonly': True}), min_value=0, initial=0)
    minutes=forms.IntegerField(widget=forms.NumberInput(attrs={'readonly': True}), min_value=0, initial=0)

    def clean(self):
        hours=self.cleaned_data.get('hours')
        minutes=self.cleaned_data.get('minutes')
        if (hours<0 or hours>12 or (minutes==0 and hours==0) or (minutes!=30 and minutes!=0)):
            raise ValidationError("Incorrect values for minutes and hours.")

    
    
