from django.db import models


# Create your models here.

class Contact(models.Model):
    phone_number = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    youtube_link = models.CharField(max_length=128)
    instagram_link = models.CharField(max_length=128)
    telegram_link = models.CharField(max_length=128)
    facebook_link = models.CharField(max_length=128)
    location_map_link = models.CharField(max_length=128)
    location_address = models.CharField(max_length=128)
