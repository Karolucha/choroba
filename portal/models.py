"""from django.db import models
from django.conf import settings
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User"""
# Create your models here.
from mongoengine import *


class Choice(EmbeddedDocument):
    choice_text = StringField(max_length=200)
    votes = IntField(default=0)


class Poll(Document):
    question = StringField(max_length=200)
    pub_date = DateTimeField(help_text='date published')
    choices = ListField(EmbeddedDocumentField(Choice))


"""
class UserRoles(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True)
    
    
class MyUser(models.Model):
    user = models.OneToOneField(User, related_name='my_user')
    birthdate = models.DateField(null=True)
    sex = models.CharField(max_length=1, null=True)
    note = models.CharField(max_length=500, null=True)
    point = models.IntegerField(null=True, default=0)
    comment_count = models.IntegerField(null=True, default=0)
    disease_added_count = models.IntegerField(null=True, default=0)
    discusion_present_count =models.IntegerField(null=True, default=0)
    role_id = models.ForeignKey(UserRoles)
    friends = models.ManyToManyField(User)
    
# TODO zastanowi� si� jakie uprawnienia
# Permission.objects.create(codename='can_add_new_place',
#                           name='Dodawanie nowego miejsca')
# Permission.objects.create(codename='can_add_comment',
#                           name='Dodawanie komentarzy')
#   Permission.objects.create(codename='can_add_new_place', name='Dodawanie nowego miejsca')
 

class Comment(models.Model):
    user = models.ForeignKey(User)
    date_publication = models.DateTimeField()
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=1000)
    time_duration = models.CharField(max_length=200, null=True)
    tips = models.CharField(max_length=200, null=True)
    points_tips = models.FloatField()
    point_comment = models.FloatField()

class Article(models.Model):
    user = models.ForeignKey(User)
    date_publication = models.DateTimeField()
    name = models.CharField(max_length=200)
    description = models.TextField()
        
class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    cure = models.CharField(max_length=1000)
    articles = models.ManyToManyField(Article)
    comments = models.ManyToManyField(Comment)
"""
