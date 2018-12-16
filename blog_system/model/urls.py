from django.urls import path
from django.conf.urls import url

from . import views

# app_name = 'blog'

urlpatterns = [
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
