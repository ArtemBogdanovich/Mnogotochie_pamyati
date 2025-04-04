from rest_framework import serializers
from .models import MapInfo

class MapInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapInfo
        fields = '__all__'
