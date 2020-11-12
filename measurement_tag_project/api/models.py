from django.db import models

# Create your models here.
class CookieModel(models.Model):
    cookie = models.CharField(max_length=20)
    visitTimes = models.IntegerField(default=0)

class HistoryModel(models.Model):
    cookie = models.CharField(max_length=20)
    datetime = models.DateTimeField()
    address = models.CharField(max_length=40)
    pageID = models.CharField(max_length=20)
    pageURL = models.CharField(max_length=200)
