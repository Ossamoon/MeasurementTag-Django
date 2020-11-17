from django.urls import path
from .views import TestPage1, TestPage2, TestPage3

urlpatterns = [
    path('1', TestPage1.as_view()),
    path('2', TestPage2.as_view()),
    path('3', TestPage3.as_view()),
]
