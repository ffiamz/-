from ..models import Blog, Category, Tag
from django import template
from django.db.models.aggregates import Count
register = template.Library()


# 可以直接在模板中使用 {% get_recent_blogs %}来调用
# 获取最新的五篇文章
@register.simple_tag
def get_recent_blogs(num=5):
    return Blog.objects.all()[:num]


# 归档模板标签，返回列表，列表中的元素为每一篇文章的创建时间
# 且是date对象，精确到月份，降序排列
@register.simple_tag
def archives():
    return Blog.objects.dates('pub', 'month', order='DESC')


# 分类模板标签
@register.simple_tag
def get_categories():
    # Count 计算分类下的文章数，其接受的参数为需要技术的模型的名称
    cate = Category.objects.all()
    for c in cate:
        if c.blog_set.count() == 0:
            c.delete()

    return Category.objects.annotate(num_posts=Count('blog')).filter(num_posts__gt=0)


# 获取标签列表
@register.simple_tag
def get_tags():
    tags = Tag.objects.all()
    for t in tags:
        if t.blog_set.count() == 0:
            t.delete()

    return Tag.objects.annotate(num_posts=Count('blog')).filter(num_posts__gt=0)


