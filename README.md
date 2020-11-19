# MeasurementTag-Django
Djangoを用いてAPIを設計し、HTML計測タグの実装をした。
また、計測タグを実装したテストページも用意した。

### 作成したAPI
| URL | 型 | 実行内容 |
|:------------|:-------:|:----------|
| api/count/ | image/png | cookieにIDを割り当てる・訪問回数をカウントする |
| api/getcount/ | text | 訪問回数またはエラー分を返す |

### 作成したタグ
###### 1. 計測用タグ
```<img src="http://localhost:8000/api/count/" alt="[画像]">```
- 計測用のタグ
- このタグを持ったページを訪れると、cookieにIDが割り当てられ訪問回数がカウントされる
- 1x1ピクセルの透明な画像がレスポンスされ、ブラウザ上に表示される

###### 2. 訪問回数取得用タグ
```
<script type="text/javascript">
    const data = document.getElementById("data");
    async function callApi() {
        const res = await fetch("http://localhost:8000/api/getcount/");
        const text = await res.text();
        data.innerHTML = text;
    }
    callApi();
</script>
```
- 訪問回数を取得し、表示するためのタグ
- Cookieに割り振られたIDがデータベースとの整合性がとれていなかった場合、エラー文を表示させる
- htmlのaタグなどにid="data"を割り当てることにより、訪問回数をブラウザ上に表示できる
- このタグを踏んでも訪問回数にはカウントされない

###### 3. 複合タグ
```
<script type="text/javascript">
    const lead1 = document.getElementById("lead1");
    const lead2 = document.getElementById("lead2");

    window.addEventListener("load", async function () {
        const res = await fetch("http://localhost:8000/api/getcount/");
        const text = await res.text();
        if (text == "1") {
            lead1.innerHTML = "こんにちは！初めてのアクセスですね！";
            lead2.innerHTML = "このページを訪れる度にアクセスした回数を記録します。";
        } else if (text.charAt(0) == 'E') {
            lead1.innerHTML = text;
            lead2.innerHTML = "エラーが検出されました。cookieやdatabaseの確認をお願いします。"
        } else {
            lead1.innerHTML = "こんにちは！" + text + "回目のアクセスですね！";
            lead2.innerHTML = "このページを訪れる度にアクセスした回数を記録します。";
        }
    })
</script>
```
- 上記2つの機能を1つにまとめたタグ
- 計測されてから訪問回数を取得するよう、JavaScriptのaddEventListenerを用いてAPI取得のタイミングを調節している
- htmlのaタグなどにid="lead1"やid="lead2"を割り当てることにより、訪問回数に応じたメッセージをブラウザ上に表示できる

### テストページ
###### テストページ１(URL: test/1/)
- 計測用タグを貼り付けたページ
###### テストページ２(URL: test/2/)
- 訪問回数取得用タグを貼り付けたページ
###### テストページ３(URL: test/3/)
- 複合タグを貼り付けたページ
