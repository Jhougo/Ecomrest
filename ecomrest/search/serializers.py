from django.forms import widgets
from rest_framework import serializers
from .models import Vehicale, People

class VehicaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicale
        fields = ('ve_vio_count', 'plate', 'vio_date', 'vio_time', 'vehicale_type', 'owner', 'vehicale_brand', 'color', 'type_detail')
class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('peo_vio_count', 'people_id', 'name', 'address', 'peo_vio_date', 'peo_vio_time')
