from django.urls import path
from .views import HomeForm, CreateUserProfileView, MyLoginView
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns=[
    #path('', views.selectgamelocation, name='home'),
    path('',HomeForm.as_view(), name='home'),
    path('placeholder/',TemplateView.as_view(template_name='placeholder.html'), name='placeholder'),
    path('locationsdisplay/',views.locationsdisplay, name='locationsdisplay'),
    #path('locationsdisplay/',TemplateView.as_view(template_name='locationsdisplay.html'), name='locationsdisplay'),
    path('detail/',views.locationdetail,name='locationdetail'),
    path('neworg/',CreateUserProfileView.as_view(), name='neworg'),
    path('login/',MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
]