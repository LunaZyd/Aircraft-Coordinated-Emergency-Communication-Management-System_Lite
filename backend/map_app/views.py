from django.shortcuts import render 
from rest_framework import generics
from .models import MapData
from .serializers import MapDataSerializer
from django.http import JsonResponse

def get_drone_position(request):
    # 模拟无人机位置数据
    drone_position = {
        'lng': 116.397428,  # 经度
        'lat': 39.90923,    # 纬度
    }
    # 返回JSON格式的无人机位置数据
    return JsonResponse(drone_position)
class MapDataListCreate(generics.ListCreateAPIView):
    queryset = MapData.objects.all()
    serializer_class = MapDataSerializer