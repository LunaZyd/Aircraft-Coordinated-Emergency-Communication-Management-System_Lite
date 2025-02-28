from django.db import models

class MapData(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()