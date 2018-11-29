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
        info = [name, theme]
        ret = rest.create_group(info)
        if ret > 0:
            return HttpResponseRedirect('/groups')
        else:
            return render(request, 'create_group.html')
    else:
        return render(request, 'create_group.html')
    



# Create your views here.
