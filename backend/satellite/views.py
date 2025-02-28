from satellite.models import SatelliteData
from satellite.serializers import SatelliteDataSerializer, SatelliteCreateUpdateDataSerializer
from dvadmin.utils.viewset import CustomModelViewSet

class SatelliteModelViewSet(CustomModelViewSet):
    """
    list: 查询无人机信息
    create: 新增无人机信息
    update: 修改无人机信息
    retrieve: 获取单个无人机信息
    destroy: 删除无人机信息
    """
    queryset = SatelliteData.objects.all()
    serializer_class = SatelliteDataSerializer
    create_serializer_class = SatelliteCreateUpdateDataSerializer
    update_serializer_class = SatelliteCreateUpdateDataSerializer
