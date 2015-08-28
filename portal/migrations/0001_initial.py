# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date_publication', models.DateTimeField()),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date_publication', models.DateTimeField()),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=1000)),
                ('time_duration', models.CharField(max_length=200, null=True)),
                ('tips', models.CharField(max_length=200, null=True)),
                ('points_tips', models.FloatField()),
                ('point_comment', models.FloatField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('cure', models.CharField(max_length=1000)),
                ('articles', models.ManyToManyField(to='portal.Article')),
                ('comments', models.ManyToManyField(to='portal.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('birthdate', models.DateField(null=True)),
                ('sex', models.CharField(max_length=1, null=True)),
                ('note', models.CharField(max_length=500, null=True)),
                ('point', models.IntegerField(default=0, null=True)),
                ('comment_count', models.IntegerField(default=0, null=True)),
                ('disease_added_count', models.IntegerField(default=0, null=True)),
                ('discusion_present_count', models.IntegerField(default=0, null=True)),
                ('friends', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='role_id',
            field=models.ForeignKey(to='portal.UserRoles'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='my_user'),
        ),
    ]
