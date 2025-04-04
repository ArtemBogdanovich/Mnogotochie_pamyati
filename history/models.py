from django.db import models


class History(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField(null=True, blank=True)
    number = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='history')
