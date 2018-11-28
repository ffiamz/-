# coding=utf8
from django.shortcuts import render
from django import forms
from model.admin import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

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

def add_user(request):
    user_id = request.POST.get('name','')
    password = request.POST.get('password','')

