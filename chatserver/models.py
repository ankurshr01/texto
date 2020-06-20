from django.db import models
from django.db import models
from django import forms
from django.conf import settings
from django.db.models.signals import post_save

class username(models.Model):
    usernames=models.TextField()

    def __str__(self):
        return self.usernames

class roomId(models.Model):
    room_name=models.TextField(max_length=100, default="-none-", help_text="Enter room number")
    
    def __str__(self):
        return self.room_name

class chatid(models.Model):
    chatroom=models.TextField(max_length=100)
    chatter = models.ForeignKey(username, on_delete=models.SET_NULL, null=True)
    roomname=models.ForeignKey(roomId, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.chatroom


