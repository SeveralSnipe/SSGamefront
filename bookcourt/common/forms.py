from django import forms
from django.db.models.base import Model
from .models import GameType
from django.forms import SelectDateWidget, ModelChoiceField, ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class HomeFormChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name
class LocationFormChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.area
class HomeForm(forms.Form):
    game=HomeFormChoiceField(queryset=GameType.objects.filter(is_active=True), label='Select Gametype')
    #location=LocationFormChoiceField(queryset=LocationArea.objects.filter(is_active=True), label='Select Area')
    date=forms.DateField(widget=SelectDateWidget(),label='Select Date')

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
        #model= TestOrganization
        fields=["phone_number"]


