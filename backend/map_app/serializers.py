from rest_framework import serializers
from .models import MapData

class MapDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapData
        fields = '__all__'
