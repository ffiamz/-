import uuid
import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, user_name, email, password=''):
        user = self.model(
                user_name = user_name,
                email = self.normalize_email(email),
                )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_name = models.CharField(max_length=30, unique=True)
    create_time = models.DateTimeField(default=datetime.datetime.now)
    email = models.EmailField()

    objects = UserManager()
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELD = ['email']
    class Meta:
        db_table = 'U'


class Team(models.Model):
    team_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=30)
    theme = models.CharField(max_length=30)
    users = models.ManyToManyField(User,through='Join')

    class Meta:
        db_table = 'T'


class Join(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)
    status = models.CharField(max_length=1, 
            choices=(('a','管理员'),('c','创建者'),('m','参与者')), default='c')
    class Meta:
        unique_together = ("team", "user")
        db_table = 'TUJR'


class Category(models.Model):
    """
    博客分类
    """
    name = models.CharField(u'名称', max_length=30)

    class Meta:
        verbose_name = u"类别"    # 给模型另起一个名字
        verbose_name_plural = verbose_name      # 定义模型的复数形式

    def __str__(self):
        return self.name

    def insert(name):
        cate = Category.objects.filter(name=name)
        if cate:
            return cate[0]
        return Category.objects.create(name=name)


class Tag(models.Model):
    name = models.CharField(u'名称', max_length=30)

    class Meta:
        verbose_name = u"标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def insert_tag(tag_list):
        tag = []
        for name in tag_list:
            name = name.strip()
            if name:
                tag.append(Tag.insert(name))
        return tag

    def insert(name):
        tag = Tag.objects.filter(name=name)
        if tag:
            return tag[0]
        return Tag.objects.create(name=name)


class Blog(models.Model):
    # 文章作者默认为管理员
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(u'标题', max_length=30)
    # author = models.CharField(u'作者', max_length=30)
    content = models.TextField(u'内容')
    pub = models.DateTimeField(u'发布时间', auto_now_add=True)
    updated = models.DateTimeField(u'更新时间', auto_now = True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=u'分类')  # 多对一（博客--类别）
    tag = models.ManyToManyField(Tag, verbose_name=u'标签', blank=True)  # (多对多）文章可以没有标签

    # 统计文章阅读量，初始为0
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name=u'博客'
        verbose_name_plural = verbose_name
        # ording 指定模型返回的数据的排列顺序
        ordering = ('-pub', )

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        # 只需更新views字段
        self.save()


class Comment(models.Model):

    name = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name=u'博客')  # （博客--评论：一对多）
    # name = models.CharField(u'称呼', max_length=30)
    # email = models.EmailField(u'邮箱')
    content = models.CharField(u'内容', max_length=200)
    pub = models.DateField(u'发布时间', auto_now_add=True)

    class Meta:
        verbose_name=u'评论'
        verbose_name_plural = u'评论'

    def __str__(self):
        return self.content


# Create your models here.
class Collection(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)
    create_time = models.DateTimeField(default=datetime.datetime.now)
    description = models.CharField(max_length=100)
    class Meta:
        unique_together = ("blog", "user")
        db_table = 'UBCR'