from .models import *
from django.shortcuts import render, HttpResponse, render_to_response, Http404, get_object_or_404
from django.http import HttpResponseRedirect

from django.db.models import Q
from .forms import CommentForm, AddBlog

import markdown


def index(request):
    return render(request, 'index.html', {'blogs': Blog.objects.all()})


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
    

def add_blog(request):
    if not request.user.is_authenticated:
        return HttpResponse("请先登录<br><a href='/login'>前往登陆</a><br><a href='/index'>返回</a>")

    if request.method == 'GET':
        blog_form = AddBlog()
        context = {'blog_form': blog_form}
        return render(request, 'blog/add_blog.html', context)
    else:
        # print(request.POST)
        blog_form = AddBlog(request.POST)
        if blog_form.is_valid():

            clearned_data = blog_form.cleaned_data
            # 文章创建默认为管理员
            # print(type(clearned_data), "\n", clearned_data)

            clearned_data['author'] = request.user
            clearned_data['category'] = Category.insert(clearned_data['category'])
            # clearned_data['category'] = Category.objects.get(id=(clearned_data['category']))
            # clearned_data['tag'] = Tag.insert_tag(request.POST.get('tag').split(','))

            tag_list = Tag.insert_tag(clearned_data['tag'].split(','))
            clearned_data.pop('tag')
            # print(clearned_data)

            blog = Blog.objects.create(**clearned_data)

            for tag in tag_list:
                blog.tag.add(tag)

            blog.save()

            # 创建完成后直接返回文章列表
            return get_blogs(request)
        else:
            return HttpResponse("表单内容有误，请重新填写.")

    # return render(request, 'blog/add_blog.html', {'form': form, 'author': author})


def delete_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()

    return get_blogs(request)


def update_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        blog_form = AddBlog(request.POST)
        if blog_form.is_valid():
            blog.title = request.POST['title']
            blog.content = request.POST['content']
            blog.category = Category.insert(request.POST['category'])

            for tag in blog.tag.all():
                blog.tag.remove(tag)
            # blog.remove_tags()
            for tag in Tag.insert_tag(request.POST['tag']):
                blog.tag.add(tag)
            # blog.insert_tags(Tag.insert(request.POST['tag']))
            blog.save()
            # 返回知道修改后的文章中
            return get_details(request, blog.id)
        else:
            return HttpResponse("表单内容有误，请重新填写")
    else:
        # 如果是get方法，创建表单类实例
        blog_form = AddBlog()
        # 赋值上下文，将article文章对象也传递进去，以便提取旧的内容
        ctx = {'blog': blog, 'blog_form': blog_form }
        return render(request, 'blog/update_blog.html', ctx)


# 展示博客列表
def get_blogs(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    # blogs = Blog.objects.all().order_by('-pub')  # 获得所有的博客按时间排序
    blogs = Blog.objects.filter(author=request.user)
    # print(blogs[0], ' ', blogs[0].author, ' ', blogs[0].content)
    return render(request, 'blog/blog_list.html', {'blogs': blogs, 'author': request.user})  


def get_index_detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)  # 获得博客对象
    except Blog.DoesNotExist:
        raise Http404
    else:
        # 阅读量加1
        blog.increase_views()
        # markdown 格式转换
        blog.content = markdown.markdown(blog.content,
                                         extensions=[
                                             # 包含 缩写、表格等常用扩展
                                             'markdown.extensions.extra',
                                             'markdown.extensions.codehilite',
                                         ])

        if request.method == 'GET':
            form = CommentForm()
        else:  # 请求方法为post

            if not request.user.is_authenticated:
                return HttpResponse("请先登录<br><a href='/login'>前往登陆</a><br><a href='/index'>返回</a>")

            form = CommentForm(request.POST)
            if form.is_valid():
                cleaned_data = form.cleaned_data
                cleaned_data['blog'] = blog

                # 评论发表默认为管理员
                # cleaned_data['name'] = User.objects.get(username='admin')
                cleaned_data['name'] = request.user
                print(type(request.user), '\n', request.user)
                Comment.objects.create(**cleaned_data)
        ctx = {
            'blog': blog,
            'comments': blog.comment_set.all().order_by('-pub'),
            'form': form
        }
        # 返回3个参数
        return render(request, 'blog/blog_index.html', ctx)


# 获取博客详细内容
def get_details(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)  # 获得博客对象
    except Blog.DoesNotExist:
        raise Http404
    else:
        # 阅读量加1
        blog.increase_views()
        # markdown 格式转换
        blog.content = markdown.markdown(blog.content,
                                         extensions=[
                                             # 包含 缩写、表格等常用扩展
                                             'markdown.extensions.extra',
                                             'markdown.extensions.codehilite',
                                         ])

        if request.method == 'GET':
            form = CommentForm()
        else:  # 请求方法为post
            form = CommentForm(request.POST)
            if form.is_valid():
                cleaned_data = form.cleaned_data
                cleaned_data['blog'] = blog

                # 评论发表默认为管理员
                # cleaned_data['name'] = User.objects.get(username='admin')
                cleaned_data['name'] = request.user

                Comment.objects.create(**cleaned_data)
        ctx = {
            'blog': blog,
            'comments': blog.comment_set.all().order_by('-pub'),
            'form': form
        }
        # 返回3个参数
        return render(request, 'blog/blog_details.html', ctx)


# 实现文章归档
def archives(request, year, month):
    post_list = Blog.objects.filter(pub__year=year,
                                    pub__month=month
                                    )
    print('year ', year, 'month', month, len(post_list))
    return render(request, 'blog/blog_list.html', {'blogs': post_list, 'author': request.user})


# 实现文章分类
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Blog.objects.filter(category=cate, author=request.user)
    return render(request, 'blog/blog_list.html', {'blogs': post_list, 'author': request.user})


# 实现标签跳转
def tag(request, pk):
    tags = get_object_or_404(Tag, pk=pk)
    post_list = Blog.objects.filter(tag=tags, author=request.user)
    return render(request, 'blog/blog_list.html', {'blogs': post_list, 'author': request.user})


def search(request):
    q = request.GET.get('q')
    # error_msg =''
    if not q:   # 如果问题为空
        error_msg = "请输入关键词"
        return render(request, 'blog/blog_list.html', {'error_msg': error_msg})
    post_list = Blog.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    return render(request, 'index.html', {'blogs': post_list, 'author': request.user})


def collect(request, blog_id):
    if not request.uesr.is_authenticated:
        return HttpResponseRedirect('/login')
    blog = Blog.objects.get(id=blog_id)
    Collect.objects.create(user=request.user, blog=blog)
    return HttpResponseRedirect('/blogs')

def collections(request):
    if not request.uesr.is_authenticated:
        return HttpResponseRedirect('/login')
    blogs = Blog.objects.filter(collection_user=request.user)
    return render(request, 'collection.html', blogs=blogs)


    


# Create your views here.
