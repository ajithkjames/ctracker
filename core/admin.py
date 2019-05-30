from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import *

# Register your models here.
admin.site.register(Branch)
admin.site.register(Sales)
# admin.site.register(Device)
admin.site.register(LocationHistory)

@admin.register(Device)
class DeviceAdmin(OSMGeoAdmin):
    list_display = ('id', 'user', 'current_location')