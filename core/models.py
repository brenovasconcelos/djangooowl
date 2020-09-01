from django.db import models

# Create your models here.
class User(models.Model):
    """
    First version of User Model
    """

    first_name = models.CharField(max_length=256, default="")
    last_name = models.CharField(max_length=256, default="")
    email = models.CharField(max_length=256, default="")
    gender = models.CharField(max_length=256, default="")
    company = models.CharField(max_length=256, default="")
    city = models.CharField(max_length=256, default="")
    title = models.CharField(max_length=256, default="")
    latitude = models.CharField(max_length=256, default="")
    longitude = models.CharField(max_length=256, default="")
