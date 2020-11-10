from django.urls import path
from .views import TestPage

urlpatterns = [
    path('', TestPage.as_view(), name = 'test'),
]
