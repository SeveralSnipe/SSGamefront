from django.urls import path
from .views import *
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns=[
    path('',HomeForm.as_view(), name='home'),
    path('placeholder/',TemplateView.as_view(template_name='placeholder.html'), name='placeholder'),
    path('locationsdisplay/',views.locationsdisplay, name='locationsdisplay'),
    path('detail/',views.locationdetail,name='locationdetail'),
    path('neworg/',OrganizationSignupView.as_view(), name='neworg'),
    path('login/',MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('days/',TimingCreate.as_view(), name='days'),
    path('profile/',TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('orgprofile/',OrganizationProfile.as_view(), name='orgprofile'),
    path('addlist/',OrganizationLocationListView.as_view(), name='addlist'),
    path('addlocation/',LocationCreateView.as_view(), name='addlocation'),
    path('addamenities/',AmenitiesView.as_view(), name='addamenities'),
    path('gametypes/',GameTypeListView.as_view(), name='gametypes'),
    path('addgametype/',GameTypeCreateView.as_view(), name = 'addgametype'),
    path('updatelocation/<int:pk>',LocationUpdateView.as_view(), name='updatelocation'),
    path("updategametype/<int:pk>", GameTypeUpdateView.as_view(), name="updategametype"),
    path("review/", PreviewPage.as_view(), name="review"),
    path("terms/", TermsPage.as_view(), name="terms"),
    path("inprogressconfirmation/", TemplateView.as_view(template_name='inprogressconfirmation.html'), name="inprogressconfirmation")
]