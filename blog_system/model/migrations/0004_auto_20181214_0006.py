# Generated by Django 2.1.2 on 2018-12-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_auto_20181129_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_group_relation',
            name='status',
            field=models.CharField(choices=[('a', '管理员'), ('c', '创建者'), ('m', '参与者')], default='c', max_length=1),
        ),
    ]
