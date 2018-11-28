import uuid
import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class User(AbstractBaseUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_name = models.CharField(max_length=30, unique=True)
    create_time = models.DateTimeField(default=datetime.datetime.now)
    email = models.EmailField()
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELD = ['email']


class UserManager(BaseUserManager):
    def create_user(self, user_name, email, password=''):
        user = self.model(
                user_name = user_name,
                email = self.normalize_email(email),
                )
        user.set_password(password)
        user.save(using=self._db)
        return user


class Blog(models.Model):
    blog_id = models.UUIDField(primary_key=True, default=uuid.uuid4)


class Group_User(models.Model):
    group_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=30),
    Theme = models.CharField(max_length=30)


class User_Blog_Collect_Relation(models.Model):
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)
    create_time = models.DateTimeField()
    description = models.CharField(max_length=100)
    class Meta:
        unique_together = ("blog_id", "user_id")


class User_Group_Relation(models.Model):
    group_id = models.ForeignKey(Group_User, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)
    status = models.CharField(max_length=1, 
            choices=(('a','管理员'),('c','创建者'),('m','成员')), default='c')
    class Meta:
        unique_together = ("group_id", "user_id")


# Create your models here.
