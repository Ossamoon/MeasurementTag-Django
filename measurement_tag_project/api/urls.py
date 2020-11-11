from django.urls import path
from .views import apifunc

urlpatterns = [
    path('', apifunc, name = 'api'),
]
