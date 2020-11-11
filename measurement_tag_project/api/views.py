from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image

# Create your views here.
def apifunc(request):
    red = Image.new('RGBA', (100, 100), (255,0,0,255))
    response = HttpResponse(content_type="image/png")
    red.save(response, "PNG")
    return response
