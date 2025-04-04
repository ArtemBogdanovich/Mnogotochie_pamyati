from django.contrib.gis.db import models


class MapInfo(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()  # Поле для хранения широты
    longitude = models.FloatField()  # Поле для хранения долготы
    icons = models.FileField(upload_to='icons/')
    history = models.TextField()
    photos = models.FileField(upload_to='photos/')
