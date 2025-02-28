from django.db import models

from dvadmin.utils.models import CoreModel


class Drone(CoreModel):
    name = models.CharField(max_length=100, verbose_name="名称", blank=False)
    registration_number = models.CharField(max_length=100, verbose_name="注册号", blank=False)
    manufacturer = models.CharField(max_length=100, verbose_name="制造商", blank=False)
    model = models.CharField(max_length=100, verbose_name="型号", blank=False)
    max_flight_altitude = models.FloatField(verbose_name="最大飞行高度", blank=False)
    max_flight_speed = models.FloatField(verbose_name="最大飞行速度", blank=False)
    max_flight_time = models.FloatField(verbose_name="最大飞行时间", blank=False)
    range = models.FloatField(verbose_name="航程", blank=False)
    max_takeoff_weight = models.FloatField(verbose_name="最大起飞重量", blank=False)
    payload_capacity = models.FloatField(verbose_name="有效载荷容量", blank=False)
    battery_type = models.CharField(max_length=100, verbose_name="电池类型", blank=True, null=True)
    gps_system = models.CharField(max_length=100, verbose_name="GPS系统", blank=True, null=True)
    communication_device = models.CharField(max_length=100, verbose_name="通信设备", blank=True, null=True)

    class Meta:
        db_table = "drones"
        verbose_name = '无人机'
        verbose_name_plural = verbose_name
        ordering = ('id',)  # 按 id 排序
