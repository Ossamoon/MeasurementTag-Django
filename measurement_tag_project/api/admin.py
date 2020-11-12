from django.contrib import admin
from .models import CookieModel, HistoryModel

# Register your models here.
admin.site.register(CookieModel)
admin.site.register(HistoryModel)
