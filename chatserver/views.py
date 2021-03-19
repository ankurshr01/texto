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
from .models import roomId,username,chatid,partt,ctr
from django.http import JsonResponse

def first(request):
    form=roomenter(request.POST)
    forms=name(request.POST)
    ct=ctr.objects.get()
    ct.counter+=1
    context={
        'form' : form,
        'forms' : forms,
        'ct' : ct,
    }
    ct.save()
    return render(request,'home.html', context)


def enterroomnumber(request):
    if request.method == "POST":
        form = roomenter(data=request.POST)
        forms=name(data=request.POST)
        dtr=chatmsg(request.POST)
        
        context={}
        if forms.is_valid() and form.is_valid(): 
            roomid=form.cleaned_data['room_name']
            room=roomId.objects.get_or_create(room_name=roomid)
            user=forms.cleaned_data['usernames']
            usr=username.objects.get_or_create(usernames=user)
            dtr=chatmsg(request.POST)
            request.session['user'] = user
            request.session['roomid'] = roomid
            lop=username.objects.get(usernames=user)
            pol=roomId.objects.get(room_name=roomid)
            ue=partt.objects.create(rom=pol,chats=lop)
            ue.save()
            context={
                'usr' : usr,
                'room' : room,
                'forms' : forms,
                'user' : user,
                'dtr' : dtr,
                'ue' : ue
            }
        return render(request,'chatroom.html',context)



def showing_chat(request):
    if request.method == 'POST':
        form = chatmsg(data=request.POST)
        dtr=chatmsg()
        if form.is_valid():
            context={}
            mess=form.cleaned_data['chatroom']
            user=request.session['user']
            roomid=request.session['roomid']
            lop=username.objects.get(usernames=user)
            pol=roomId.objects.get(room_name=roomid)
            msg=chatid.objects.create(chatroom=mess,chatter=lop,roomname=pol)
            msg.save()
            messa=chatid.objects.filter(roomname=pol)
            context={
                'mess' : mess,
                'messa' : messa,
                'dtr' : dtr,
                'siz' : siz,
            }
            dtr=chatmsg()
        
        return render(request,'chatroom.html',context)


def chat_sender(request):
    cht=chatid()
    user=request.session['user']
    roomid=request.session['roomid']
    lop=username.objects.get(usernames=user)
    pol=roomId.objects.get(room_name=roomid)
    cht.chatroom=request.GET['chat']
    cht.chatter=lop
    cht.roomname=pol
    cht.save()
    return JsonResponse({'response':True},safe= False)


def showchat(request):
    roomid=request.session['roomid']
    pol=roomId.objects.get(room_name=roomid)
    mes=chatid.objects.filter(roomname=pol)
    usr=request.session['user']
    up=partt.objects.filter(rom=pol)
    context={
        'usr' : usr,
        'mes' : mes,
        'up' : up,
    }
    return render(request,'fetch.html',context)