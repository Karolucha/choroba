"""from django.db import models
from django.conf import settings
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User"""
# Create your models here.
import datetime
from mongoengine import *
#from django_mongoengine.auth.models import User
from mongoengine.django.auth import User
print(connect('misiowa'))


class UserRoles(Document):
    name = StringField()
    description = StringField(null=True)


class Image(Document):
    date_publication = DateTimeField()
    img = ImageField()
    description = StringField(max_length=500, null=True)


class MyUser(Document):
    user = ReferenceField(User)
    birthdate = DateTimeField(null=True)
    sex = StringField(max_length=1, null=True)
    note = StringField(max_length=500, null=True)
    point = FloatField(null=True, default=0.0)
    comment_count = IntField(null=True, default=0)
    disease_added_count = IntField(null=True, default=0)
    article_added_count = IntField(null=True, default=0)
    discussion_added_count = IntField(null=True, default=0)
    forum_present_count = IntField(null=True, default=0)
    image = ImageField(collection_name="profile")
    register_date = DateTimeField(default=datetime.datetime.now)
    images = ListField(ReferenceField(Image))

    roles = ListField(ReferenceField(UserRoles))
    comments = ListField(ReferenceField('Comment'))
    articles = ListField(ReferenceField('Article'))
    diseases = ListField(ReferenceField('Disease'))
    friends = ListField(ReferenceField('self'))
    IsPublicProp = DictField()
  #  for prop in ('self').my_metaclass.get_all_field_names():
  #      IsPublicProp[prop] = False

    def has_perm(self, perm):
        if perm in self.roles:
            return True



class PublicTerms(Document):
    name = StringField()
    code = StringField()


class Invitation(Document):
    inviting = ReferenceField(MyUser)
    invited = ReferenceField(User)
    discussion = ReferenceField(MyUser, null=True)


class CommentCategory(Document):
    name = StringField()


class Comment(Document):
    user = ReferenceField(MyUser)
    date_publication = DateTimeField(default=datetime.datetime.now)
    name = StringField(max_length=200, null=True)
    description = StringField(max_length=1000)
    unit_duration = StringField(max_length=200, null=True)
    value_duration = StringField(max_length=200, null=True)
    age = IntField(null=True)
    tips = StringField(max_length=200, null=True)
    points_tips = FloatField(null=True, default=0.0)
    point_comment = FloatField(null=True, default=0.0)
    image = ImageField(collection_name="comment", null=True)
    category = ReferenceField(CommentCategory)
    disease = ReferenceField('Disease', null=True)


class Forum(Document):
    name = StringField(max_length=100)
    description = StringField(max_length=1000, null=True)
    comments = ListField(ReferenceField(Comment))
    images = ListField(ImageField(collection_name="forum"))
    founder = ReferenceField('MyUser')
    meta = {'allow_inheritance': True}


class Disease(Forum):
    cure = StringField(max_length=1000, null=True)
    articles = ListField(ReferenceField('Article'))
    images = ListField(ImageField(collection_name="disease"))


class Discussion(Forum):
    users = ListField(ReferenceField('MyUser'))
    public_term = ReferenceField('PublicTerms')
    date_register = DateTimeField(default=datetime.datetime.now)


class Article(Document):
    founder = ReferenceField(MyUser)
    date_publication = DateTimeField(default=datetime.datetime.now)
    last_modification = DateTimeField(default=datetime.datetime.now)
    name = StringField(max_length=200)
    description = StringField()
    images = ListField(ImageField(collection_name="article"))


# userRole = UserRoles(name='normal')
# userRole.save()
# userRole = UserRoles(name='admin')
# userRole.save()
#
# user = MyUser(username='bob', password='bobpass')
# user.save()
#
# disease =Disease(name='alergia: roztocze', description='kazdy na to cierpi')
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
 

"""
