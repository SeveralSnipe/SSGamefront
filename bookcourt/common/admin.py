from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Tenant)
admin.site.register(TenantUser)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Area)
admin.site.register(Customer)
admin.site.register(Organization)
admin.site.register(OrganizationLocation)
admin.site.register(OrganizationLocationGameType)
admin.site.register(GameType)
admin.site.register(OrganizationLocationAmenities)
admin.site.register(OrganizationLocationWorkingTime)
admin.site.register(OrganizationGameImages)