from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from PIL import Image

# Create your views here.
def apicountfunc(request):
    cookie = "cookie_test_2"
    try:
        print(request.COOKIES[cookie])
    except:
        print('not have test cookie')
    print(request.META['REMOTE_ADDR'])
    red = Image.new('RGBA', (100, 100), (255,0,0,255))
    response = HttpResponse(content_type="image/png")
    red.save(response, "PNG")
    response.set_cookie(key=cookie, value='005')
    print("set cookie")
    return response
