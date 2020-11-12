from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from PIL import Image

# Create your views here.
def apicountfunc(request):
    # cookieの名前を定義
    cookie = "cookie_test_2"

    # cookieを取得
    try:
        print(request.COOKIES[cookie])
    except:
        print('not have test cookie')

    # クライアントのIPアドレスを取得
    print(request.META['REMOTE_ADDR'])

    # レスポンスを作成
    red = Image.new('RGBA', (100, 100), (255,0,0,255))
    response = HttpResponse(content_type="image/png")
    red.save(response, "PNG")

    # レスポンスにcookieを設定
    response.set_cookie(key=cookie, value='005')
    print("set cookie")

    # レスポンスを返す
    return response
