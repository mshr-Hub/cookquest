from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from .models import CustomUser, Quest, Message

import datetime
import pytz
import json

# 非同期関連のアクション管理

@require_POST
def ajax_message_create(request, pk):
    message_text = request.POST['message_text']
    message_image = request.FILES.get('message_image', '')
    customuser_name = request.POST['author']
    author = CustomUser.objects.get(username=customuser_name)
    quest_id = request.POST['quest']
    quest = Quest.objects.get(pk=quest_id)
    if message_text == '' and message_image == '':
        return redirect('message_index', pk=pk)
    message = Message.objects.create(text=message_text, image=message_image, author=author, quest=quest)

    if message.image:
        post_image = message.image.url
    else:
        post_image = None
    message_dict = {
        'message_text': message.text,
        'message_image': post_image,
        'author': customuser_name,
        'created_at': message.created_at.now(pytz.timezone('Asia/Tokyo')).strftime("%Y年%-m月%d日%H:%M"),
    }
    return JsonResponse(message_dict)