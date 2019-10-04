from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Quest, Message

# Register your models here.

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Quest)
admin.site.register(Message)
