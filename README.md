# CookQUEST(クックエスト)について
「ワクワクしながら使える遊び心のあるアプリ」をコンセプトに、料理好きな人だけが使うアプリとしてではなく、このアプリをきっかけに料理に興味を持つ人が増えれば嬉しいと思い作成しました。現在、多数のレシピアプリやSNS上の料理動画のおかげで、美味しい料理を簡単に作れる時代になりました。しかし、レシピや動画だけではどうしても理解しにくい部分が料理にあるのも、また事実です。このアプリでは、そんな料理の世界に飛び込んだばかりの新米が抱える料理の分かりにくい部分を、先輩たちへの質問やコミュニケーションを通して解決できます。それだけではなく、現実ではなかなか料理のコミュニティが見つけられない方も、このアプリでは気軽にコミュニティを見つけて、参加する事ができます。是非、あなたも「CookQUEST」の世界に参加して、ご自身の料理レベルをアップさせてみてください！！……という紹介が付けられそうな雰囲気になっています。

### 《開発環境》
- Python, Django, bootstrap, jQuery, Heroku, S3
- 仮想環境の構築はAnacondaで行いました。

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
- belongs_to :Quest
