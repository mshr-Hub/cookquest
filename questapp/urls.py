from django.urls import path, include
from .views import toppage, quest_index, quest_create, quest_detail, quest_delete, quest_update, quest_search, app_login, app_signup, app_logout, mypage, message_index
from .ajax import ajax_message_create

urlpatterns = [
  path('', toppage, name='toppage'),

  path('index/', quest_index, name='index'),
  path('create/', quest_create, name='create'),
  path('detail/<int:pk>', quest_detail, name='detail'),
  path('delete/<int:pk>', quest_delete, name='delete'),
  path('update/<int:pk>', quest_update, name='update'),
  path('search/', quest_search, name='search'),

  path('login/', app_login, name='login'),
  path('signup/', app_signup, name='signup'),
  path('logout/', app_logout, name='logout'),
  path('mypage/<int:pk>', mypage, name='mypage'),

  path('detail/<int:pk>/', include([
    path('messages/', message_index, name='message_index'),
    path('ajax_message_create/', ajax_message_create, name='message_create'),
  ])),
]
