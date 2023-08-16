from django import forms
from django.db.models.base import Model
from .models import GameType, LocationArea
from django.forms import SelectDateWidget, ModelChoiceField

class HomeFormChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name
class LocationFormChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.area
class HomeForm(forms.Form):
    game=HomeFormChoiceField(queryset=GameType.objects.filter(is_active=True), label='Select Gametype')
    location=LocationFormChoiceField(queryset=LocationArea.objects.filter(is_active=True), label='Select Area')
    date=forms.DateField(widget=SelectDateWidget(),label='Select Date')



