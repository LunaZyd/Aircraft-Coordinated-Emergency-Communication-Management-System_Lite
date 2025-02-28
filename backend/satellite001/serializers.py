# from satellite001.models import formdataModel
# from dvadmin.utils.serializers import CustomModelSerializer
# from rest_framework import serializers
# from rest_framework.decorators import action, permission_classes
# from rest_framework.permissions import IsAuthenticated
#
# class FormdataModelSerializer(CustomModelSerializer):
#     """
#     序列化器
#     """
#
#     class Meta:
#         model = formdataModel
#         fields = "__all__"
#
#
# class FormdataModelCreateUpdateSerializer(CustomModelSerializer):
#     """
#     创建/更新时的列化器
#     """
#
#     class Meta:
#         model = formdataModel
#         fields = '__all__'
#
# """
# 导出
# """
# class ExportFormdataModelSerializer(CustomModelSerializer):
#     """
#        信息导出 序列化器
#     """
#
#     class Meta:
#         model = formdataModel
#         fields = (
#             "community",
#             "building",
#             "unit",
#             "door_number",
#             "network_operator",
#             "broadband_account",
#             "mobile_phone",
#             "member1_consumption",
#             "member2_consumption",
#             "member3_consumption",
#             "business_expiration_date",
#             "num_of_members",
#             "decision_maker_age",
#         )
from rest_framework import serializers
from .models import SatelliteData

class SatelliteDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SatelliteData
        fields = ['id', 'latitude', 'longitude', 'message', 'signal_strength', 'device_id', 'communication_channel']
