# coding=utf8
from django.shortcuts import render
from django import forms
from model.admin import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from .models import Blog

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/index')
    else:
        form = UserCreationForm()
    context = {}
    context['title'] = '注册'
    context['form'] = form
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # return render(request, '/index', {'blogs': Blog.objects.all()})
            return HttpResponseRedirect('/index')
        else:
            return HttpResponseRedirect('/login')
    else:
        return render(request, 'login.html')

        
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/index")
