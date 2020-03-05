from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    hris_id = models.CharField(max_length=5, blank=False, verbose_name='HRIS ID')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
