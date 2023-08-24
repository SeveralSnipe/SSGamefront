from django import forms
from django.db.models.base import Model
from .models import *
from django.forms import SelectDateWidget, ModelChoiceField, ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from smart_selects.form_fields import ChainedModelChoiceField

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


class CustomUserCreationForm(UserCreationForm):  
    username = forms.CharField(label='Organization Name', min_length=5, max_length=150)
    first_name= forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)  
    email = forms.EmailField(label='Organization Email')  
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
  
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email    
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        return user
class OrganizationProfileForm(forms.ModelForm):
    class Meta:
        model= Organization
        fields=["phone_number"]


