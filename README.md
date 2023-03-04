 # gptindexを用いて、Webサイトの情報のembeddingを行える　discord-chatbotの作成

discord内で、chatGPTのように対話できるbotを作成しました。

最近、chatGPTが流行っていますが、直近のデータや専門的な情報は、学習されていません。
そこで、それぞれのdiscordにて、学習させたい専門的な、情報を学習させられるように、GPTindexを用いてカスタマイズしました。

```javascript
必要なパッケージをインストール
pip install gpt_index

envファイルの設定
cp env.example


指定したurlのページを学習させる (ここでは、OpenAIのapikeyと、指定したいwebsiteのurlを.env常に設定することができます。)
python save.py



自分の指定した質問をする(ここで、QUESTION変数をいじることで、プロンプトの会話内容をターミナルで試すことができます。)
python load.py



discordに、botを招待。(developerpageにて、discordbotのAPIを取得して、下記コマンドを実行可能にします。)
参考　：https://note.com/npaka/n/n2ea2a6dda0e5


botを起動
python example_bot.py


node_modules/web3/dist/web3.min.js (33:26729)\
```
下記が.envの設定のテンプレートです。

```sh:ENV
MYAPI='xxxxxxxxxxxx-openAIのkey'
THEURL="https://docs.coffin.finance/"
QUESTION1="xxxxを、簡単に教えてください？"
DISCORDTOKEN="xxxxxxxxxxxxxxdiscordのdeveloperpageのtoken"

```




memo

必要なパッケージをインストール

pip install ---


envファイルの設定
env.exampleをコピーして、.envファイルとし、下記の変数に適切な情報を入力していきます。
MYAPI,THEURL,QUESTION1,(DISCORDTOKEN)etc.....


指定したurlのページを学習させる
python save.py


自分の指定した質問をする
python load.py


discordに、botを招待。
参考https://note.com/npaka/n/n2ea2a6dda0e5

.envファイルにて、discordtokenの設定

botを起動
python example_bot.py

