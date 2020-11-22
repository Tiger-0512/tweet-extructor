# Twitter日本語評判分析データセットからツイートを取得，抽出

[Twitter日本語評判分析データセット](http://bigdata.naist.jp/~ysuzuki/data/twitter/)にて配布されているデータセットのうち，2つ以上の項目が1となっているデータ，Tweet内容が取得できないデータを除き，csvファイルとして取得するためのコードです．

100ツイートを一度に取得する方法に関しては、[Twitter日本語評判分析データセットのためのツイートダウンローダ](https://github.com/tatHi/tweet_extructor/)を参考にさせていただきました．

<br>

## 使い方

### データセットCSVのダウンロード

[Twitter日本語評判分析データセット](http://bigdata.naist.jp/~ysuzuki/data/twitter/)にて配布されているtweets_open.csvファイルをダウンロード．

### TwitterAPPの登録
[twitterAPI](https://apps.twitter.com/)を用いるため，適当なアプリをtwitter appに登録し，
API Key, API Key Secret, Access Token, Access Token Secretを取得してください．<br>

取得したキーはget_tweets.py内の以下のxxxに書き込んでください．

```
CK = 'xxx' # API Key
CS = 'xxx' # API Key Secret
AT = 'xxx' # Access Token
AS = 'xxx' # Access Token Secret
```

### 実行
run.pyと同じ場所にcsvファイルをおいて，以下を実行してください．
アノテーション情報と，対応するツイートのテキストがcsv形式で吐き出されます．

```
$ python run.py
```

Tweetをjson, pickleで取得したい場合，2_tweetExecutor.py内のコメントアウトを外してください．

### 注意
API制限の関係で，1秒あたりに100ツイートのみの取得となります．（run.pyを実行する場合は気にする必要はありません）
データセットに含まれるツイート数から単純に計算して，全てのデータをダウンロードするのに2時間弱必要になります．
