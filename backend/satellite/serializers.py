from satellite.models import SatelliteData
from dvadmin.utils.serializers import CustomModelSerializer

class SatelliteDataSerializer(CustomModelSerializer):

    class Meta:
        model = SatelliteData
        fields = "__all__"
class SatelliteCreateUpdateDataSerializer(CustomModelSerializer):
    """
    创建/更新无人机信息序列化器
    """

    class Meta:
        model = SatelliteData
        fields = "__all__"
