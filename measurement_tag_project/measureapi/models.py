from django.db import models

# Create your models here.
class Track(models.Model):
    trackID = models.CharField(max_length=32)
    datetime = models.DateTimeField()
    address = models.CharField(max_length=32)
