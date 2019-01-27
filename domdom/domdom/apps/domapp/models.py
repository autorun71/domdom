from django.db import models
import datetime
# Create your models here.

class StaticPage(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255, default='')
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, default='')
    h1 = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    text = models.TextField(default='')
    text2 = models.TextField(default='')
    belon = models.BigIntegerField(default=0)
    enable = models.BigIntegerField(default=0)

    def __str__(self):
        return str(self.id) + "_" + str(self.title)

class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255, default='')
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, default='')
    h1 = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    text = models.TextField(default='')
    belon = models.BigIntegerField(default=0)
    enable = models.BigIntegerField(default=0)

    def __str__(self):
        return str(self.id) + "_" + str(self.title)

class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255, default='')
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, default='')
    h1 = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    text = models.TextField(default='')
    price = models.BigIntegerField(default=0)
    oldprice = models.BigIntegerField(default=0)
    belon = models.BigIntegerField(default=0)
    enable = models.BigIntegerField(default=0)

    def __str__(self):
        return str(self.id) + "_" + str(self.title)

