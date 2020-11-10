from rest_framework import generics

from .models import Track
from .serializer import TrackSerializer

class TrackViewSet(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
