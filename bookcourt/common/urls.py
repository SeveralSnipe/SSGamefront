from django.urls import path
from .views import HomeForm, CreateUserProfileView
from django.views.generic import TemplateView
from . import views

urlpatterns=[
    #path('', views.selectgamelocation, name='home'),
    path('',HomeForm.as_view(), name='home'),
    path('placeholder/',TemplateView.as_view(template_name='placeholder.html'), name='placeholder'),
    path('locationsdisplay/',views.locationsdisplay, name='locationsdisplay'),
    #path('locationsdisplay/',TemplateView.as_view(template_name='locationsdisplay.html'), name='locationsdisplay'),
    path('detail/',views.locationdetail,name='locationdetail'),
    path('neworg/',CreateUserProfileView.as_view(), name='neworg')
]