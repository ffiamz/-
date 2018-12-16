from django import forms

from .models import Blog
# 收集评论, 借此完成博客的评论功能


class CommentForm(forms.Form):

    content = forms.CharField(label='内容', error_messages={
        'required': '请填写您的评论内容',
        'max_length': '评论内容太长了'
    })


class AddBlog(forms.Form):
    # title =
    title = forms.CharField(label=u'标题', max_length=30, error_messages={
        'required': '请填写您的标题',
        'max_length': '标题太长了'
    })
    # content = forms.TextField()
    category = forms.CharField(label=u'类别', max_length=30)
    # category = forms.IntegerField()
    tag = forms.CharField(max_length=150)

    content = forms.CharField(widget=forms.Textarea)
