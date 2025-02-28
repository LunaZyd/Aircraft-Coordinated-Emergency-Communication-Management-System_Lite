from drones.models import Drone
from drones.serializers import DroneSerializer, DroneCreateUpdateSerializer, ExportDroneSerializer
from dvadmin.utils.viewset import CustomModelViewSet

class DroneModelViewSet(CustomModelViewSet):
    """
    list: 查询无人机信息
    create: 新增无人机信息
    update: 修改无人机信息
    retrieve: 获取单个无人机信息
    destroy: 删除无人机信息
    """
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    create_serializer_class = DroneCreateUpdateSerializer
    update_serializer_class = DroneCreateUpdateSerializer

    # 导出字段数据
    export_field_data = [
        "name", "registration_number", "manufacturer", "model", "max_flight_altitude",
        "max_flight_speed", "max_flight_time", "range", "max_takeoff_weight",
        "payload_capacity", "battery_type", "gps_system", "communication_device"
    ]

    # 导出字段标签
    export_field_label = {
        "name": "名称",
        "registration_number": "注册号",
        "manufacturer": "生产厂家",
        "model": "型号",
        "max_flight_altitude": "最大飞行高度",
        "max_flight_speed": "最大飞行速度",
        "max_flight_time": "最大飞行时间",
        "range": "航程范围",
        "max_takeoff_weight": "最大起飞重量",
        "payload_capacity": "负载能力",
        "battery_type": "电池类型",
        "gps_system": "GPS系统",
        "communication_device": "通信设备"
    }

    # 导出序列化器
    export_serializer_class = ExportDroneSerializer
