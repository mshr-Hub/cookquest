from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    pass


class Quest(models.Model):
    title = models.CharField(max_length=100)
    memo = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='', blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="create_quest")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='', blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="create_message")
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name="quest_message")
    created_at = models.DateTimeField(auto_now_add=True)

