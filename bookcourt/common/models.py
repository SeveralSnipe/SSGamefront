from django.utils import timezone
from datetime import datetime, date
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from booking.models import *
from smart_selects.db_fields import ChainedForeignKey
#from location_field.models.plain import LocationField


# class Tenant(models.Model):
#     name=models.CharField(max_length=100)
#     sign_up_terms_and_conditions=models.TextField()
#     booking_terms_and_conditions=models.TextField()
#     #location=models.CharField(max_length=100)
#     is_active=models.BooleanField(default=True)

#     # def __str__(self):
#     #     return self.name

# class Customer(User):
# 	tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT)
#     #name = models.CharField(max_length=100)
# 	#organization_membership_mapping = models.ManytoManyField( , through='CustomerOrganizationMapping')
    
# class Organization(User):
#     tenant=models.ForeignKey(Tenant, on_delete=models.PROTECT)
#     organization_name=models.CharField(max_length=100)
#     alt_number=models.PositiveBigIntegerField()
#     description=models.TextField(max_length=None)
#     is_terms_and_conditions_agreed=models.BooleanField(default=False)
#     status=models.IntegerField(choices=status_choices, default= PENDING)

#     # def __str__(self):
#     #     return self.name

# class OrganizationLocation(models.Model):
#     organization=models.ForeignKey(Organization, on_delete=models.PROTECT)
#     #location = models.CharField(max_length=255)
#     #location_in_map = models.LocationField(based_fields=['location_from_map'], zoom=7)
#     address_line_1=models.TextField(max_length=255)
#     address_line_2=models.TextField(max_length=255)
#     area=models.TextField(max_length=50)
#     city=models.TextField(max_length=50)
#     state=models.TextField(max_length=50)
#     pincode=models.IntegerField()
#     contact_number=models.PositiveBigIntegerField()
#     #work_from_time=models.DateTimeField()
#     #work_to_time=models.DateTimeField()
#     join_date = models.DateField()
#     created_date = models.DateField(auto_now=True)
#     created_time = models.DateTimeField(auto_now=True)
#     is_active=models.BooleanField(default=False)

#     # def __str__(self):
#     #     return self.org_id.name

# class LocationCity(models.Model):
#     tenant=models.ForeignKey(Tenant, on_delete=models.PROTECT)
#     city= models.CharField(max_length=100)
#     is_active=models.BooleanField(default=True)

# class LocationArea(models.Model):
#     tenant=models.ForeignKey(Tenant,on_delete=models.PROTECT)
#     city_name=models.ForeignKey(LocationCity,on_delete=models.PROTECT)
#     area=models.CharField(max_length=100)
#     is_active=models.BooleanField(default=True)

# class GameType(models.Model):
#     name=models.CharField(max_length=100)
#     is_active=models.BooleanField(default=True)

#     # def __str__(self):
#     #     return self.name

# class OrganizationLocationAmenities(models.Model):
#     organization_location=models.OneToOneField(OrganizationLocation, on_delete=models.PROTECT)
#     is_parking=models.BooleanField(default=False)
#     is_restrooms=models.BooleanField(default=False)
#     is_changerooms=models.BooleanField(default=False)
#     is_powerbackup=models.BooleanField(default=False)
#     is_beverages_facility=models.BooleanField(default=False)
#     is_coaching_facilities=models.BooleanField(default=False)
#     description= models.TextField()

#     # def __str__(self):
#     #     return self.org_loc_id.org_id.name
    
# class OrganizationLocationGameType(models.Model):
#     organization_location=models.ForeignKey(OrganizationLocation, on_delete=models.PROTECT)
#     game_type=models.ForeignKey(GameType, on_delete=models.PROTECT)
#     pricing=models.DecimalField(decimal_places=2,max_digits=10)
#     # price_calculate_timing=models.IntegerField()
#     is_active=models.BooleanField(default=False)
#     description=models.TextField()

#     # def __str__(self):
#     #     return self.org_loc_id.org_id.name+self.game_type.name
    
# class OrganizationLocationWorkingDays(models.Model):
#     organization=models.OneToOneField(OrganizationLocation, on_delete=models.PROTECT)
#     is_monday_workingday = models.BooleanField(default=True)
#     is_tuesday_workingday = models.BooleanField(default=True)
#     is_wednesday_workingday = models.BooleanField(default=True)
#     is_thursday_workingday = models.BooleanField(default=True)
#     is_friday_workingday = models.BooleanField(default=True)
#     is_saturday_workingday = models.BooleanField(default=True)
#     is_sunday_workingday = models.BooleanField(default=True)

#     def check_working(self,day):
#         match day:
#             case 'Monday':
#                 return self.is_monday_workingday
#             case 'Tuesday':
#                 return self.is_tuesday_workingday
#             case 'Wednesday':
#                 return self.is_wednesday_workingday
#             case 'Thursday':
#                 return self.is_thursday_workingday
#             case 'Friday':
#                 return self.is_friday_workingday
#             case 'Saturday':
#                 return self.is_saturday_workingday
#             case 'Sunday':
#                 return self.is_sunday_workingday
            

#     # def __str__(self):
#     #     return self.org_loc_id.org_id.name

# class OrganizationGameImages(models.Model):
#     organization=models.ForeignKey(OrganizationLocationGameType, on_delete=models.PROTECT)
#     image=models.ImageField(upload_to='uploads/')

#     # def __str__(self):
#     #     return self.org.org_loc_id.org_id.name+self.org.game_type.name

# class TestCustomer(models.Model):
#     user=models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
#     tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT)
#     #name = models.CharField(max_length=100)
# 	#organization_membership_mapping = models.ManytoManyField( , through='CustomerOrganizationMapping')
    
# class TestOrganization(models.Model):
#     user=models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
#     tenant=models.ForeignKey(Tenant, on_delete=models.PROTECT)
#     organization_name=models.CharField(max_length=100, default="No Organization name set")
#     phone_number=models.PositiveBigIntegerField(default=None)
#     description=models.TextField(max_length=None, default="No Description set")
#     is_terms_and_conditions_agreed=models.BooleanField(default=False)
#     status=models.IntegerField(choices=status_choices, default= PENDING)

#     # def __str__(self):
#     #     return self.name

# class TestOrganizationLocation(models.Model):
#     organization=models.ForeignKey(TestOrganization, on_delete=models.PROTECT)
#     #location = models.CharField(max_length=255)
#     #location_in_map = models.LocationField(based_fields=['location_from_map'], zoom=7)
#     address_line_1=models.TextField(max_length=255)
#     address_line_2=models.TextField(max_length=255)
#     area=models.TextField(max_length=50)
#     city=models.TextField(max_length=50)
#     state=models.TextField(max_length=50)
#     pincode=models.IntegerField()
#     contact_number=models.PositiveBigIntegerField()
#     #work_from_time=models.DateTimeField()
#     #work_to_time=models.DateTimeField()
#     join_date = models.DateField()
#     created_date = models.DateField(auto_now=True)
#     created_time = models.DateTimeField(auto_now=True)
#     is_active=models.BooleanField(default=False)

#     # def __str__(self):
#     #     return self.org_id.name

# class TestLocationCity(models.Model):
#     tenant=models.ForeignKey(Tenant, on_delete=models.PROTECT)
#     city= models.CharField(max_length=100)
#     is_active=models.BooleanField(default=True)

# class TestLocationArea(models.Model):
#     tenant=models.ForeignKey(Tenant,on_delete=models.PROTECT)
#     city_name=models.ForeignKey(TestLocationCity,on_delete=models.PROTECT)
#     area=models.CharField(max_length=100)
#     is_active=models.BooleanField(default=True)

# class TestOrganizationLocationAmenities(models.Model):
#     organization_location=models.OneToOneField(TestOrganizationLocation, on_delete=models.PROTECT)
#     is_parking=models.BooleanField(default=False)
#     is_restrooms=models.BooleanField(default=False)
#     is_changerooms=models.BooleanField(default=False)
#     is_powerbackup=models.BooleanField(default=False)
#     is_beverages_facility=models.BooleanField(default=False)
#     is_coaching_facilities=models.BooleanField(default=False)
#     description= models.TextField()

#     # def __str__(self):
#     #     return self.org_loc_id.org_id.name
    
# class TestOrganizationLocationGameType(models.Model):
#     organization_location=models.ForeignKey(TestOrganizationLocation, on_delete=models.PROTECT)
#     game_type=models.ForeignKey(GameType, on_delete=models.PROTECT)
#     pricing=models.DecimalField(decimal_places=2,max_digits=10)
#     # price_calculate_timing=models.IntegerField()
#     is_active=models.BooleanField(default=False)
#     description=models.TextField()

#     # def __str__(self):
#     #     return self.org_loc_id.org_id.name+self.game_type.name
    
# class TestOrganizationLocationWorkingDays(models.Model):
#     organization=models.OneToOneField(TestOrganizationLocation, on_delete=models.PROTECT)
#     is_monday_workingday = models.BooleanField(default=True)
#     is_tuesday_workingday = models.BooleanField(default=True)
#     is_wednesday_workingday = models.BooleanField(default=True)
#     is_thursday_workingday = models.BooleanField(default=True)
#     is_friday_workingday = models.BooleanField(default=True)
#     is_saturday_workingday = models.BooleanField(default=True)
#     is_sunday_workingday = models.BooleanField(default=True)

#     def check_working(self,day):
#         match day:
#             case 'Monday':
#                 return self.is_monday_workingday
#             case 'Tuesday':
#                 return self.is_tuesday_workingday
#             case 'Wednesday':
#                 return self.is_wednesday_workingday
#             case 'Thursday':
#                 return self.is_thursday_workingday
#             case 'Friday':
#                 return self.is_friday_workingday
#             case 'Saturday':
#                 return self.is_saturday_workingday
#             case 'Sunday':
#                 return self.is_sunday_workingday
            

#     # def __str__(self):
#     #     return self.org_loc_id.org_id.name


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
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
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
    work_day_choices=models.CharField(max_length=10, choices= day_choices)
    from_time=models.TimeField()
    to_time=models.TimeField()
    is_active=models.BooleanField(default=True)

# class OrganizationLocationWorkingDays(models.Model):
#     SUNDAY = 0
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     day_choices = (
#         (SUNDAY, 'Sunday'),
#         (MONDAY, 'Monday'),
#         (TUESDAY, 'Tuesday'),
#         (WEDNESDAY, 'Wednesday'),
#         (THURSDAY, 'Thursday'),
#         (FRIDAY, 'Friday'),
#         (SATURDAY, 'Saturday'),
#         )
#     organization_location=models.ForeignKey(OrganizationLocation, on_delete=models.CASCADE)
#     days=models.IntegerField(choices=day_choices)
#     work_from_time=models.TimeField()
#     work_to_time=models.TimeField()
#     is_active=models.BooleanField(default=True)

# class OrganizationLocationWorkingTime(models.Model):
#     organization=models.ForeignKey(OrganizationLocation, on_delete=models.CASCADE)
#     primary_from_time=models.TimeField()
#     primary_to_time=models.TimeField()
#     secondary_from_time=models.TimeField(null=True,blank=True)
#     secondary_to_time=models.TimeField(null=True,blank=True)
    
#     def stringify_time(self, choice):
#         if choice==1:
#             return self.primary_from_time+'-'+self.primary_to_time
#         else:
#             return self.secondary_from_time+'-'+self.secondary_to_time
   
# class OrganizationLocationWorkingDay(models.Model):
#     SUNDAY = 0
#     MONDAY = 1
#     TUESDAY = 2
#     WEDNESDAY = 3
#     THURSDAY = 4
#     FRIDAY = 5
#     SATURDAY = 6
#     day_choices = (
#         (SUNDAY, 'Sunday'),
#         (MONDAY, 'Monday'),
#         (TUESDAY, 'Tuesday'),
#         (WEDNESDAY, 'Wednesday'),
#         (THURSDAY, 'Thursday'),
#         (FRIDAY, 'Friday'),
#         (SATURDAY, 'Saturday'),
#         )
#     # PRIMARY = 0
#     # SECONDARY = 1
#     # time_choices = (
#     #     (PRIMARY, 'Primary Time Slot'),
#     #     (SECONDARY, 'Secondary Time Slot')
#     # )
    
#     workingtimes=models.ForeignKey(OrganizationLocationWorkingTime, on_delete=models.CASCADE)
#     day=models.IntegerField(choices=day_choices)
#     timing=models.BooleanField()
#     # def get_times(self):
#     #     return (
#     #         (1, self.workingtimes.stringify(1)),
#     #         (2, self.workingtimes.stringify(2)),
#     #         )
    
    
    
    
class OrganizationGameImages(models.Model):
    organization=models.ForeignKey(OrganizationLocationGameType, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='uploads/')
    is_active=models.BooleanField(default=True)


    




