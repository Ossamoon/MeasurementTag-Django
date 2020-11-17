import datetime
from django.utils.timezone import make_aware
import uuid
from PIL import Image
from django.http import HttpResponse
from .models import CookieModel, HistoryModel


# Create your views here.
def apicountfunc(request):
    # cookieのkeyとvalueを定義
    cookie_key = "measurement_tag_project_ossamoon_12"
    cookie_value = "temp"  # valueの値は仮置き

    # レスポンスを作成
    red = Image.new('RGBA', (100, 100), (255, 0, 0, 255))
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
        datetime_now = make_aware(datetime.datetime.now())
        # リファラページを取得
        referer_page = request.META['HTTP_REFERER']
        # HistoryModelに新規登録
        HistoryModel.objects.create(cookie=cookie_value, datetime=datetime_now, address=client_address,
                                    pageURL=referer_page)
        print("create new object at HistoryModel")
        # 訪問回数(CookieModel.visitTimes)を1だけ上げる
        item = CookieModel.objects.get(cookie=cookie_value)
        item.visitTimes += 1
        item.save()
    elif count == 0:
        print("Cookie Error: Cookie has an unknown value.")
    else:
        print("Database Error: Cookie_value has double (or more) booked in CookieModel")

    # レスポンスを返す
    return response


def apigetcountfunc(request):
    # cookieのkeyとvalueを定義
    cookie_key = "measurement_tag_project_ossamoon_12"
    cookie_value = "temp"

    # レスポンスを作成
    response = HttpResponse()

    if cookie_key in request.COOKIES.keys():
        cookie_value = request.COOKIES[cookie_key]
        # cookie_valueがCookieModelに1件だけ登録されているかどうかをチェック
        exact_entry = CookieModel.objects.filter(cookie__exact=cookie_value)
        count = exact_entry.count()
        if count == 1:
            # 訪問回数をレスポンスに代入
            item = CookieModel.objects.get(cookie=cookie_value)
            response.write(f"<p>{item.visitTimes}</p>")
        elif count == 0:
            response.write("<p>Error:NoCookieValue</p>")
        else:
            response.write("<p>Error:DoubledCookieValue</p>")
    else:
        response.write("<p>Error:NoCookieKey</p>")

    # レスポンスを返す
    return response
