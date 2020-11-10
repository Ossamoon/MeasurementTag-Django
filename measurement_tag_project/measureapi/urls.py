from django.urls import path
from .views import TrackViewSet

urlpatterns = [
    path('', TrackViewSet.as_view()),
]
