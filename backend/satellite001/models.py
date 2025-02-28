# from django.db import models
# from dvadmin.utils.models import CoreModel


from django.db import models

class SatelliteData(models.Model):
    latitude = models.FloatField(help_text="纬度")
    longitude = models.FloatField(help_text="经度")
    message_content = models.TextField(help_text="消息内容")
    signal_strength = models.FloatField(null=True, blank=True, help_text="信号强度（可选）")
    device_id = models.CharField(max_length=50, help_text="设备ID（标识符）")
    communication_channel = models.CharField(max_length=50, null=True, blank=True, help_text="通信信道（可选）")

    def __str__(self):
        return f"SatelliteData {self.id}: {self.message_content}"



#
# class formdataModel(CoreModel):
#     community = models.CharField(max_length=100, verbose_name="小区", blank=False)
#     building = models.IntegerField(verbose_name="楼幢", blank=False)
#     unit = models.IntegerField(verbose_name="单元", blank=False)
#     door_number = models.IntegerField(verbose_name="门牌", blank=False)
#     network_operator = models.CharField(max_length=100, verbose_name="网络运营商", blank=True, null=True)
#     broadband_account = models.CharField(max_length=100, verbose_name="DX手机号码（宽带账号）", blank=True, null=True)
#     mobile_phone = models.CharField(max_length=100, verbose_name="YD手机号码", blank=True, null=True)
#     member1_consumption = models.FloatField(verbose_name="家庭成员1消费", blank=False)
#     member2_consumption = models.FloatField(verbose_name="家庭成员2消费", blank=True, null=True)
#     member3_consumption = models.FloatField(verbose_name="家庭成员3消费", blank=True, null=True)
#     business_expiration_date = models.DateField(verbose_name="商机到期时间", blank=True, null=True)
#     num_of_members = models.IntegerField(verbose_name="家庭成员人数", blank=False)
#     decision_maker_age = models.IntegerField(verbose_name="决策人年龄", blank=True, null=True)
#
#     class Meta:
#         db_table = "formdatas"
#         verbose_name = '表单数据'
#         verbose_name_plural = verbose_name
#         ordering = ('id',)  # 按 id 排序
