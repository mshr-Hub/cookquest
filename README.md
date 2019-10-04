# DB設計

## Customusers
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


# CookQuest(クックエスト)について
https://docs.google.com/presentation/d/e/2PACX-1vRJMo_Mwfkywpc0dguZPPLx-d-kPLWyAIIIix0UOfGo9TEpSdu8VYMjEVf-PKcuBPnWMSpRrtn5xGK6/embed?start=false&loop=false&delayms=10000
