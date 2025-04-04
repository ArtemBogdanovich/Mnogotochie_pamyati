from django.db import models
from django.urls import reverse


class Person(models.Model):
    name = models.CharField(max_length=50)
    post = models.CharField(max_length=150)
    role = models.CharField(max_length=160)
    history = models.TextField()
    image = models.ImageField(blank=True, upload_to='person')
    photo1 = models.ImageField(blank=True, upload_to='person')

    def __str__(self):
        return self.name



