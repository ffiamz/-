from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import rest

def index(request):
    return render(request, 'index.html')

def users(request):
    us = rest.get_all_users()
    return render(request, 'users.html', 
            {'users': us})

def groups(request):
    gs = rest.get_all_groups()
    return render(request, 'groups.html',
            {'groups': gs})

def create_group(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    if request.method == 'POST':
        name = request.POST.get('name','')
        theme = request.POST.get('theme', '')
        info = [name, theme, request.user.user_id]
        ret = rest.create_group(info)
        if ret > 0:
            return HttpResponseRedirect('/groups')
    return render(request, 'create_group.html')

def join_group(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    if request.method == 'GET':
        user_id = request.user.user_id
        group_id = request.GET.get('group_id')
        ret = rest.add_user_into_group([user_id, group_id])
    return HttpResponseRedirect('/groups')

def delete_group():
    pass

def collect_blog():
    pass

def remove_blog_from_collect():
    pass
    



# Create your views here.
