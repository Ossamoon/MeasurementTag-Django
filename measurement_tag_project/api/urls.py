from django.urls import path
from .views import apicountfunc, apigetcountfunc

urlpatterns = [
    path('count/', apicountfunc),
    path('getcount/', apigetcountfunc),
]
