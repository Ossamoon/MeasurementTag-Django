from django.db import models

# Create your models here.
class CookieModel(models.Model):
    cookie = models.CharField(max_length=50)
    visitTimes = models.IntegerField(default=0)

class HistoryModel(models.Model):
    cookie = models.CharField(max_length=50)
    datetime = models.DateTimeField()
    address = models.CharField(max_length=50)
    pageURL = models.CharField(max_length=200)
