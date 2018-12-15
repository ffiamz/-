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


class Blog(models.Model):
    blog_id = models.UUIDField(primary_key=True, default=uuid.uuid4)


class Team(models.Model):
    team_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=30)
    theme = models.CharField(max_length=30)
    users = models.ManyToManyField(User,through='Join')
    class Meta:
        db_table = 'T'


class Collection(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)
    create_time = models.DateTimeField(default=datetime.datetime.now)
    description = models.CharField(max_length=100)
    class Meta:
        unique_together = ("blog", "user")
        db_table = 'UBCR'


class Join(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)
    status = models.CharField(max_length=1, 
            choices=(('a','管理员'),('c','创建者'),('m','参与者')), default='c')
    class Meta:
        unique_together = ("team", "user")
        db_table = 'TUJR'


# Create your models here.
