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

# Create your models here.
