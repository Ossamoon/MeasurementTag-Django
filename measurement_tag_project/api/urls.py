from django.urls import path
from .views import apicountfunc

urlpatterns = [
    path('count/', apicountfunc, name = 'count'),
]
