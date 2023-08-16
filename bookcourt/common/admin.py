from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Tenant)
admin.site.register(Customer)
admin.site.register(Organization)
admin.site.register(OrganizationLocationGameType)
admin.site.register(GameType)
admin.site.register(OrganizationLocationAmenities)
admin.site.register(OrganizationLocationWorkingDays)
admin.site.register(OrganizationGameImages)