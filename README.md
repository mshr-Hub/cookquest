# CookQUEST(クックエスト)について
「ワクワクしながら使える遊び心のあるアプリ」をコンセプトに、料理好きな人だけが使うアプリとしてではなく、このアプリをきっかけに料理に興味を持つ人が増えれば嬉しいと思い作成しました。現在、多数のレシピアプリやSNS上の料理動画のおかげで、美味しい料理を簡単に作れる時代になりました。しかし、レシピや動画だけではどうしても理解しにくい部分が料理にあるのも、また事実です。このアプリでは、そんな料理の世界に飛び込んだばかりの新米「勇者」が抱える料理の分かりにくい部分を、経験豊富な「勇者」への質問やコミュニケーションを通して解決できます。それだけではなく、現実ではなかなか料理のコミュニティが見つけられない方も、このアプリでは気軽にコミュニティを見つけて、参加する事ができます。是非、あなたも「CookQUEST」の世界に参加して、ご自身の料理レベルをアップさせてみてください！！……という紹介が付けられそうな雰囲気になっています。


## **本番環境**
<a href="https://cookquest.herokuapp.com/" target="_blank">CookQUEST</a>

### 《テストユーザーのログイン情報》
- ユーザー名：勇者ヨシヒコ
- 秘密の呪文(パスワード)：hogefuga1

### 《動作確認方法》
- Chromeの最新版を利用してアクセスしてください。
  - ただしデプロイ等で接続できないタイミングもございます。その際は少し時間をおいてから接続ください。
- 接続先およびログイン情報については、上記の通りです。
- 同時に複数の方がログインしている場合に、ログインできない可能性がございます。
- 確認後、ログアウト処理をお願いします。

### 《改善ポイント》
- ユーザーのアバター登録
- 各ユーザーの詳細ページを表示、フレンド機能
- パーティー機能（プライベートなコミュニティ機能）
- クエストクリア機能（参考になったコメントへのいいね）
- メッセージ画面の自動更新


# DB設計

## CustomUsers
|Column|Type|Options|
|------|----|-------|
|username|CharField|max_length=150, unique=True|
|email|CharField|blank=True, max_length=254|

### Association
- has_many :Quests
- has_many :Messages


## Quests
|Column|Type|Options|
|------|----|-------|
|title|CharField|max_length=100|
|memo|CharField|max_length=100|
|text|TextField||
|image|ImageField|upload_to='', blank=True, null=True|
|author|ForeignKey|CustomUser, on_delete=models.CASCADE, related_name="create_quest"|
|created_at|DateTimeField|auto_now_add=True|
|updated_at|DateTimeField|auto_now=True|

### Association
- belongs_to :Customuser
- has_many :Messages


## Messages
|Column|Type|Options|
|------|----|-------|
|text|TextField|blank=True, null=True|
|image|ImageField|upload_to='', blank=True, null=True|
|author|ForeignKey|CustomUser, on_delete=models.CASCADE, related_name="create_message"|
|quest|ForeignKey|Quest, on_delete=models.CASCADE, related_name="quest_message"|
|created_at|DateTimeField|auto_now_add=True|

### Association
- belongs_to :Customuser
- belongs_to :Qusts