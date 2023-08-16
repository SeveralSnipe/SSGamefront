from django.utils import timezone
from datetime import datetime, date
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from booking.models import *
#from location_field.models.plain import LocationField


APPROVED = 1
PENDING = 2
IN_PROGRESS = 3
CANCELLED = 4
status_choices =(
	    (APPROVED, 'Approved'),
	    (PENDING, 'Pending'),
	    (IN_PROGRESS, 'In Progress'),
	    (CANCELLED, 'Cancelled'),
    )


class Tenant(models.Model):
    name=models.CharField(max_length=100)
    sign_up_terms_and_conditions=models.TextField()
    booking_terms_and_conditions=models.TextField()
    #location=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

    # def __str__(self):
    #     return self.name

class Customer(User):
	tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT)
    #name = models.CharField(max_length=100)
	#organization_membership_mapping = models.ManytoManyField( , through='CustomerOrganizationMapping')
    
class Organization(User):
    tenant=models.ForeignKey(Tenant, on_delete=models.PROTECT)
    organization_name=models.CharField(max_length=100)
    alt_number=models.PositiveBigIntegerField()
    description=models.TextField(max_length=None)
    is_terms_and_conditions_agreed=models.BooleanField(default=False)
    status=models.IntegerField(choices=status_choices, default= PENDING)

    # def __str__(self):
    #     return self.name

class OrganizationLocation(models.Model):
    organization=models.ForeignKey(Organization, on_delete=models.PROTECT)
    #location = models.CharField(max_length=255)
    #location_in_map = models.LocationField(based_fields=['location_from_map'], zoom=7)
    address_line_1=models.TextField(max_length=255)
    address_line_2=models.TextField(max_length=255)
    area=models.TextField(max_length=50)
    city=models.TextField(max_length=50)
    state=models.TextField(max_length=50)
    pincode=models.IntegerField()
    contact_number=models.PositiveBigIntegerField()
    #work_from_time=models.DateTimeField()
    #work_to_time=models.DateTimeField()
    join_date = models.DateField()
    created_date = models.DateField(auto_now=True)
    created_time = models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=False)

    # def __str__(self):
    #     return self.org_id.name

class LocationCity(models.Model):
    tenant=models.ForeignKey(Tenant, on_delete=models.PROTECT)
    city= models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

class LocationArea(models.Model):
    tenant=models.ForeignKey(Tenant,on_delete=models.PROTECT)
    city_name=models.ForeignKey(LocationCity,on_delete=models.PROTECT)
    area=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

class GameType(models.Model):
    name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)

    # def __str__(self):
    #     return self.name

class OrganizationLocationAmenities(models.Model):
    organization_location=models.ForeignKey(OrganizationLocation, on_delete=models.PROTECT)
    is_parking=models.BooleanField(default=False)
    is_restrooms=models.BooleanField(default=False)
    is_changerooms=models.BooleanField(default=False)
    is_powerbackup=models.BooleanField(default=False)
    is_beverages_facility=models.BooleanField(default=False)
    is_coaching_facilities=models.BooleanField(default=False)
    description= models.TextField()

    # def __str__(self):
    #     return self.org_loc_id.org_id.name
    
class OrganizationLocationGameType(models.Model):
    organization_location=models.ForeignKey(OrganizationLocation, on_delete=models.PROTECT)
    game_type=models.ForeignKey(GameType, on_delete=models.PROTECT)
    pricing=models.DecimalField(decimal_places=2,max_digits=10)
    # price_calculate_timing=models.IntegerField()
    is_active=models.BooleanField(default=False)
    description=models.TextField()

    # def __str__(self):
    #     return self.org_loc_id.org_id.name+self.game_type.name
    
class OrganizationLocationWorkingDays(models.Model):
    organization=models.ForeignKey(OrganizationLocation, on_delete=models.PROTECT)
    is_monday_workingday = models.BooleanField(default=True)
    is_tuesday_workingday = models.BooleanField(default=True)
    is_wednesday_workingday = models.BooleanField(default=True)
    is_thursday_workingday = models.BooleanField(default=True)
    is_friday_workingday = models.BooleanField(default=True)
    is_saturday_workingday = models.BooleanField(default=True)
    is_sunday_workingday = models.BooleanField(default=True)

    def check_working(self,day):
        match day:
            case 'Monday':
                return self.is_monday_workingday
            case 'Tuesday':
                return self.is_tuesday_workingday
            case 'Wednesday':
                return self.is_wednesday_workingday
            case 'Thursday':
                return self.is_thursday_workingday
            case 'Friday':
                return self.is_friday_workingday
            case 'Saturday':
                return self.is_saturday_workingday
            case 'Sunday':
                return self.is_monday_workingday
            

    # def __str__(self):
    #     return self.org_loc_id.org_id.name

class OrganizationGameImages(models.Model):
    organization=models.ForeignKey(OrganizationLocationGameType, on_delete=models.PROTECT)
    image=models.ImageField(upload_to='uploads/')

    # def __str__(self):
    #     return self.org.org_loc_id.org_id.name+self.org.game_type.name

