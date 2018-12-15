from .models import *
from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html')

def users(request):
    us = User.objects.all()
    return render(request, 'users.html', 
            {'users': us})

def teams(request):
    gs = Team.objects.all()
    return render(request, 'teams.html',
            {'teams': gs})

def create_team(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    if request.method == 'POST':
        name = request.POST.get('name','')
        theme = request.POST.get('theme', '')
        team = Team.objects.create(name=name, theme=theme)
        Join.objects.create(user=request.user, team=team, status='c')
        return HttpResponseRedirect('/teams')
    return render(request, 'create_team.html')

def team(request, team_id):
    try:
        team = Team.objects.get(team_id=team_id)
        creator = User.objects.get(team=team, join__status='c')
        members = User.objects.filter(team=team, join__status='m')
        status = 'n'
        if request.user.is_authenticated:
            cur = Join.objects.filter(team=team, user=request.user)
            if cur.exists():
                status = cur.first().status
        else:
            status = 'nu'
    except:
        return HttpResponseRedirect('/teams')
    return render(request, 'team.html', {'team':team, 'creator':creator,
        'members':members, 'status':status })


def join_team(request, team_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    try:
        team = Team.objects.get(team_id=team_id)
        Join.objects.create(user=request.user, team=team, status='m')
    except:
        pass
    return HttpResponseRedirect('/team/%s'%team_id)

def leave_team(request, team_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    try:
        team = Team.objects.get(team_id=team_id)
        Join.objects.filter(user=request.user,team=team).delete()
    except:
        pass
    return HttpResponseRedirect('/team/%s'%team_id)


def delete_team(request, team_id):
    team=Team.objects.get(team_id=team_id)
    if Join.objects.get(user=request.user,team=team).status == 'c':
        team.delete()


def collect_blog():
    pass

def remove_blog_from_collect():
    pass
    



# Create your views here.
