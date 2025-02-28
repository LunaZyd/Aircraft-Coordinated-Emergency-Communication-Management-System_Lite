# from satellite001.models import formdataModel
# from satellite001.serializers import FormdataModelSerializer, FormdataModelCreateUpdateSerializer, ExportFormdataModelSerializer
# from dvadmin.utils.viewset import CustomModelViewSet

from rest_framework import viewsets
from rest_framework.response import Response
from .models import SatelliteData
from .serializers import SatelliteDataSerializer

# class FormdataModelViewSet(CustomModelViewSet):
#     """
#     list:查询
#     create:新增
#     update:修改
#     retrieve:单例
#     destroy:删除
#     """
#     queryset = formdataModel.objects.all()
#     serializer_class = FormdataModelSerializer
#     create_serializer_class = FormdataModelCreateUpdateSerializer
#     update_serializer_class = FormdataModelCreateUpdateSerializer
#     # YD手机号码  DX手机号码
#     # filter_fields = ['community', 'building', 'broadband_account', 'mobile_phone']
#     # search_fields = ['community']
#     class Meta:
#         model = formdataModel
#         fields = ['community', 'building', 'broadband_account', 'mobile_phone']
#
#     export_field_data = ['小区', '楼幢', '单元', '门牌', '网络运营商', 'DX手机号码',
#                          'YD手机号码', '家庭成员1消费', '家庭成员2消费', '家庭成员3消费',
#                          '商机到期时间', '家庭成员人数', '决策人年龄', '家庭成员3消费', ]
#
#
#
#     export_serializer_class = ExportFormdataModelSerializer

class SatelliteDataViewSet(viewsets.ModelViewSet):
    queryset = SatelliteData.objects.all()
    serializer_class = SatelliteDataSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
