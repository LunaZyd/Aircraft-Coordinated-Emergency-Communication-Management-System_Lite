from drones.models import Drone
# from rest_framework import serializers
from dvadmin.utils.serializers import CustomModelSerializer


class DroneSerializer(CustomModelSerializer):
    """
    无人机信息序列化器
    """

    class Meta:
        model = Drone
        fields = "__all__"

class DroneCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新无人机信息序列化器
    """

    class Meta:
        model = Drone
        fields = '__all__'

class ExportDroneSerializer(CustomModelSerializer):
    """
    导出无人机信息序列化器
    """

    class Meta:
        model = Drone
        fields = (
            "name",
            "registration_number",
            "manufacturer",
            "model",
            "max_flight_altitude",
            "max_flight_speed",
            "max_flight_time",
            "range",
            "max_takeoff_weight",
            "payload_capacity",
            "battery_type",
            "gps_system",
            "communication_device",
        )
