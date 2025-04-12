from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=55)
    picture = models.ImageField(upload_to='company_picture/', null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    telegram = models.CharField(max_length=55, null=True, blank=True)
    instagram = models.CharField(max_length=55, null=True, blank=True)
    linkedin = models.CharField(max_length=55, null=True, blank=True)
    about_us = models.TextField()