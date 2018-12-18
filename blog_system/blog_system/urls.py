"""BlogSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from model import views, user

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^index$', views.index),

    url(r'^teams$', views.teams),
    url(r'^create_team$', views.create_team),
    path('team/<uuid:team_id>', views.team),
    path('join_team/<uuid:team_id>', views.join_team),
    path('leave_team/<uuid:team_id>', views.leave_team),

    url(r'^users$', views.users),
    url(r'^register$', user.register),
    url(r'^login$', user.login),
    url(r'^logout$', user.logout),

    path('collect/<uuid:team_id>',views.collect),
    url('collections',views.collections),
    
    #path('blog/', include('model.urls')),
    
    path('', views.get_blogs, name='blog_view'),
    path('create-blog/', views.add_blog, name="add_blog"),
    path('detail/<int:blog_id>', views.get_details, name='blog_get_detail'),
    path('delete/<int:blog_id>', views.delete_blog, name="delete_blog"),
    path('update/<int:blog_id>', views.update_blog, name="update_blog"),
    path('archives/<int:year>/<int:month>', views.archives, name="archives"),
    path('category/<int:pk>', views.category, name='category'),
    path('tag/<int:pk>', views.tag, name="tag"),
    path('search/', views.search, name='search'),
    # path('add_tag/', views.add_tag, name="add_tag"),
    # path('add_category/', views.add_category, name="add_category"),
    path('index/<int:blog_id>', views.get_index_detail, name="blog_index"),
]
