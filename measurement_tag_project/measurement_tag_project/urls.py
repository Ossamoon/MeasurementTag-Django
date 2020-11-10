from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('measureapi.urls')),
    path('test/', include('testpage.urls')),
]
