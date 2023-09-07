from django.db import models
from django.contrib.auth.models import User
from booking.models import *
#from location_field.models.plain import LocationField
#MODEL REVISION 23/8/23
class Tenant(models.Model):
    tenant_name=models.CharField(max_length=100)
    sign_up_terms_and_conditions=models.TextField()
    booking_terms_and_conditions=models.TextField()
    
    def __str__(self):
        return self.tenant_name
    
class TenantUser(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT)
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.username

class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT)
    phone_number=models.PositiveBigIntegerField(default=None)
    is_active=models.BooleanField(default=True)    
	#organization_membership_mapping = models.ManytoManyField( , through='CustomerOrganizationMapping')

    def __str__(self):
        return self.user.username


class Country(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT)
    country_name=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.country_name

class State(models.Model):
    country=models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.state_name


class City(models.Model):
    state=models.ForeignKey(State, on_delete=models.CASCADE)
    city_name=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.city_name

class Area(models.Model):
    city=models.ForeignKey(City, on_delete=models.CASCADE)
    area_name=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.area_name

    
class GameType(models.Model):
    game_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.game_name

class Organization(models.Model):
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
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    tenant=models.ForeignKey(Tenant, on_delete=models.PROTECT)
    organization_name=models.CharField(max_length=100, blank=True, null=True, default=None)
    phone_number=models.PositiveBigIntegerField(blank=True, null=True, default=None)
    alt_number=models.PositiveBigIntegerField(blank=True, null=True, default=None)
    description=models.TextField(blank=True, null=True, default=None)
    is_terms_and_conditions_agreed=models.BooleanField(default=False)
    status=models.IntegerField(choices=status_choices, default= PENDING)
    is_active=models.BooleanField(default=True)
    created_date=models.DateField(auto_now=True)
    approved_date=models.DateField(null=True,blank=True)
    
    def __str__(self):
        return self.user.username

class OrganizationLocation(models.Model):
    organization=models.ForeignKey(Organization, on_delete=models.CASCADE)
    #location = models.CharField(max_length=255)
    #location_in_map = models.LocationField(based_fields=['location_from_map'], zoom=7)
    address_line_1=models.TextField()
    address_line_2=models.TextField()
    area=models.ForeignKey(Area, on_delete=models.PROTECT, null=True)
    pincode=models.IntegerField()
    phone_number=models.PositiveBigIntegerField()
    join_date = models.DateField(null=True, blank=True)
    created_date_time = models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    
    # def __str__(self):
    #     return self.organization.user.username
  
class OrganizationLocationAmenities(models.Model):
    organization_location=models.OneToOneField(OrganizationLocation, on_delete=models.CASCADE)
    is_parking=models.BooleanField(default=False)
    is_restrooms=models.BooleanField(default=False)
    is_changerooms=models.BooleanField(default=False)
    is_powerbackup=models.BooleanField(default=False)
    is_beverages_facility=models.BooleanField(default=False)
    is_coaching_facilities=models.BooleanField(default=False)
    description= models.TextField()
    is_active=models.BooleanField(default=True)

    # def __str__(self):
    #     return self.organization_location__username 

class OrganizationLocationGameType(models.Model):
    organization_location=models.ForeignKey(OrganizationLocation, on_delete=models.CASCADE)
    game_type=models.ForeignKey(GameType, on_delete=models.PROTECT)
    pricing=models.DecimalField(decimal_places=2,max_digits=10)
    # price_calculate_timing=models.IntegerField()
    description=models.TextField()
    is_active=models.BooleanField(default=True)
    
    
class OrganizationLocationWorkingTime(models.Model):
    WORK_DAY_CHOICES = 'work_day_choices'
    
    day_choices = (
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        )
    organization_location= models.ForeignKey(OrganizationLocation, on_delete=models.CASCADE)
    work_day_choices=models.CharField(max_length=10, choices= day_choices, blank=True)
    from_time=models.TimeField(null=True, blank=True)
    to_time=models.TimeField(null=True, blank=True)
    is_active=models.BooleanField(default=True)

class OrganizationGameImages(models.Model):
    organization=models.ForeignKey(OrganizationLocationGameType, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='uploads/')
    is_active=models.BooleanField(default=True)


    




