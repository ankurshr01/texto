from django import forms
from django.contrib.auth.models import User
from .models import roomId,username,chatid
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class roomenter(forms.ModelForm):
    class Meta:
        model=roomId
        fields=['room_name']
        widgets = {
            'room_name' : forms.TextInput(attrs={' placehoder ':' Enter room number ', 'class':'input'})
        }

class name(forms.ModelForm):
    class Meta:
        model=username
        fields=['usernames']
        widgets = {
            'usernames' : forms.TextInput(attrs={' placehoder ':' Enter username ', 'class':'input'})
        }

class chatmsg(forms.ModelForm):
    class Meta:
        model=chatid
        fields=['chatroom']
        widgets = {
            'chatroom' : forms.TextInput(attrs={'id':'chatidd'})
        }

