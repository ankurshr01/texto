from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash	
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMultiAlternatives 
from django.contrib import messages 
from django.core.mail import send_mail 
from django.template.loader import get_template 
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from .forms import roomenter,name,chatmsg
from .models import roomId,username,chatid

def first(request):
    form=roomenter(request.POST)
    forms=name(request.POST)
    context={
        'form' : form,
        'forms' : forms
    }
    return render(request,'home.html', context)

rom=""

def enterroomnumber(request):
    if request.method == "POST":
        form = roomenter(data=request.POST)
        forms=name(data=request.POST)
        if forms.is_valid() and form.is_valid(): 
            roomid=form.cleaned_data['room_name']
            rom=roomid
            room=roomId.objects.get_or_create(room_name=roomid)
            user=forms.cleaned_data['usernames']
            usr=username.objects.get_or_create(usernames=user)
            dtr=chatmsg(request.POST)
            rom=roomid
            context={
                'usr' : usr,
                'room' : room,
                'forms' : forms,
                'user' : user,
                'dtr' : dtr
            }
            return render(request,'chatroom.html',context)


def showchat(request):
    if request.method == 'POST':
        users=name(data=request.POST)
        form = chatmsg(data=request.POST)
        usr = roomenter(data=request.POST)
        print(rom)
        if form.is_valid(): 
            mess=form.cleaned_data['chatroom']
            # use=users.cleaned_data['usernames']
            # print(use)

            msg=chatid.objects.create(chatroom=form)

            msg.save()  
            return render(request,'chatroom.html')

    

