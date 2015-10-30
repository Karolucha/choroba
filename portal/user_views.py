
from django.shortcuts import render_to_response, redirect
from portal.models import *
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

import mongoengine

#mongoengine.connect('misiowa')
from mongoengine.django.auth import User
import pprint


# def change_profile(request):
#     if (request.POST):
#         user=User.objects.get(id=request.user.id)
#         my_user=MyUser.objects.get(user=user)
#         if(request.POST['surname']):
#             my_user.user.surname=request.POST['surname']
#         # if(request.POST['birthday']):
#         #     my_user.birthdate=request.POST['birthday']
#         my_user.save()
#         return render_to_response('profile/account.html',{'my_user': my_user}, RequestContext(request))
#     else:
#         users_from_database = User.objects.all()
#         return render_to_response('profile/account.html',{'users_from_database': users_from_database}, RequestContext(request))

def logging(request):
    username = request.POST['username']
    password = request.POST['password']
    print("username")
    print(username)
    print("password")
    print(password)

 #   User.create_user(username=request.POST['username'], email='random3@pi.pl', password=request.POST['password'])
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            print("Logged as user: "+str(user))
            return redirect(request.META['HTTP_REFERER'], context_instance=RequestContext(request))
        else:
            print("cant logged user")
            # Return a 'disabled account' error message
    else:
        pass
        # Return an 'invalid login' error message.
    print("Tried to log as user: "+str(user))
    return redirect(request.META['HTTP_REFERER'], context_instance=RequestContext(request))

def logouting(request):
    logout(request)
    # Redirect to a errors page.
    return redirect(request.META['HTTP_REFERER'], context_instance=RequestContext(request))

def add_friend(request, user_id):
    logout(request)
    # Redirect to a errors page.
    return redirect(request.META['HTTP_REFERER'], context_instance=RequestContext(request))

def profile(request, user_id):
    user = User.objects.get(id=request.user.id)
    my_user = MyUser.objects.get(user=user)

    if (request.POST):

        # if(request.POST['surname']):
        #     my_user.user.surname=request.POST['surname']
        # # if(request.POST['birthday']):
        # #     my_user.birthdate=request.POST['birthday']
       # my_user.save()
        return render_to_response('profile/profile.html', {'my_user': my_user}, RequestContext(request))
    else:
        return render_to_response('profile/profile.html', {'my_user': my_user}, RequestContext(request))

def register(request):
    # errors = []
    # if(request.POST.get('password','1') != request.POST.get('confirm_password','1')):
    #     errors.append('wrong_password')
    # if(request.POST.get('username', "field is empty") == "" or request.POST.get('email', "field is empty") == "" or request.POST.get('password',"field is empty") == ""):
    #     errors.append('empty_field')
    # if(len(errors) != 0):
    #     return render_to_response('profile/register.html', {'errors': errors}, RequestContext(request))
    # else:
    users_from_database = User.objects.all()
    if request.POST:
        User.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        my_user = MyUser()
        my_user.user = user
        my_user.save()
        login(request, user)

        return render_to_response('profile/account.html',{'users': users_from_database}, RequestContext(request))
    else:
        return render_to_response('profile/register.html',{'users': users_from_database}, RequestContext(request))



def get_all_users():
    all_users = MyUser.objects.all()
    return all_users
@login_required
def account(request):
    all_users = MyUser.objects.all()
    print(all_users)
    print("tu zyja userzy")
    if (request.POST):
        user = User.objects.get(id=request.user.id)
        my_user = MyUser.objects.get(user=user)
        if(request.POST['surname']):
            my_user.user.surname=request.POST['surname']
        # if(request.POST['birthday']):
        #     my_user.birthdate=request.POST['birthday']
        my_user.save()
        return render_to_response('profile/account.html',{'my_user': my_user,'all_users': all_users}, RequestContext(request))
    else:
        user = User.objects.get(id=request.user.id)
        my_user = MyUser.objects.get(user=user)
        return render_to_response('profile/account.html', {'my_user': my_user, 'all_users': all_users}, RequestContext(request))
