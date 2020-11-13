import datetime
import uuid
from PIL import Image

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.db.models import TextField
from django.db.models.functions import Cast

from .models import CookieModel, HistoryModel

# Create your views here.
def apicountfunc(request):
    # cookieのkeyとvalueを定義
    cookie_key = "measurement_tag_project_ossamoon_11"
    cookie_value = "temp"   # valueの値は仮置き

    # レスポンスを作成
    red = Image.new('RGBA', (100, 100), (255,0,0,255))
    response = HttpResponse(content_type="image/png")
    red.save(response, "PNG")


    # 該当するcookieを所持しているかチェック
    if cookie_key in request.COOKIES.keys():
        # cookieの値を取得
        cookie_value = request.COOKIES[cookie_key]
    else:
        # 新しいvalueをUUIDを用いて発行
        cookie_value = str(uuid.uuid4())
        # CookieModelに新規登録
        CookieModel.objects.create(cookie=cookie_value, visitTimes=0)
        print("create new object at CookieModel")
        # レスポンスにcookieを設定
        response.set_cookie(key=cookie_key, value=cookie_value)
        print("set cookie to response")

    # cookie_valueがCookieModelに1件だけ登録されているかどうかをチェック
    exact_entry = CookieModel.objects.filter(cookie__exact=cookie_value)
    count = exact_entry.count()
    if count == 1:
        # IPアドレスを取得
        client_address = request.META['REMOTE_ADDR']
        # 現在の日時を取得
        datetime_now = datetime.datetime.now()
        # HistoryModelに新規登録
        HistoryModel.objects.create(cookie = cookie_value, datetime = datetime_now, address = client_address, pageURL = "url")
        print("create new object at HistoryModel")
        # 訪問回数(CookieModel.visitTimes)を1だけ上げる
        item = CookieModel.objects.get(cookie=cookie_value)
        item.visitTimes += 1
        item.save()
    elif count == 0:
        print("Cookie Error: Cookie has an unkvown value.")
    else:
        print("Database Error: Cookie_value has double (or more) booked in CookieModel")

    # レスポンスを返す
    return response
