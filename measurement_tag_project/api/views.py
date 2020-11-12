import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from PIL import Image
from .models import CookieModel, HistoryModel

# Create your views here.
def apicountfunc(request):
    # cookieの名前を定義
    cookie_key = "measurement_tag_project_ossamoon"

    # imageデータとレスポンスを作成
    red = Image.new('RGBA', (100, 100), (255,0,0,255))
    response = HttpResponse(content_type="image/png")
    red.save(response, "PNG")

    # クライアントが該当するcookieを所持しているかどうか
    if "measurement_tag_project_ossamoon" in request.COOKIES.keys():
        cookie_value = request.COOKIES[cookie_key]
        exact_entry = CookieModel.objects.filter(cookie__exact=cookie_value)
        count = exact_entry.count()
        if count == 1:
            # HistoryModelに新しいレコードを追加
            client_address = request.META['REMOTE_ADDR']
            print(client_address)
            datetime_now = datetime.datetime.now()
            print(datetime_now)
            HistoryModel.objects.create(cookie = cookie_value, datetime = datetime_now, address = client_address, pageURL = "url")
            print("Add new object to HistoryModel")
            # 訪問回数(CookieModel.visitTimes)を1だけ上げる
            item = CookieModel.objects.get(cookie=cookie_value)
            item.visitTimes += 1
            item.save()
            print("visitTimes += 1")
        elif count == 0:
            print("Cookie Error: Cookie has an unkvown value.")
        else:
            print("Database Error: Cookie_value has double (or more) booked in CookieModel")

    else:
        pass
        # ユーザーつくらなきゃ

    # レスポンスにcookieを設定
    response.set_cookie(key=cookie_key, value='004')
    print("set cookie")

    # レスポンスを返す
    return response
