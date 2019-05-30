from rest_framework import serializers
from .models import *
from drf_extra_fields.geo_fields import PointField

class DeviceSerializer(serializers.ModelSerializer):
    current_location = PointField()
    class Meta:
        model = Device
        fields = ('id', 'user', 'current_location')