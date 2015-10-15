
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



def logging(request):
    username = request.POST['username']
    password = request.POST['password']

    User.create_user(username=request.POST['username'], email='random3@pi.pl', password=request.POST['password'])
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            print("Logged as user: "+str(user))
            return redirect(request.META['HTTP_REFERER'], context_instance=RequestContext(request))
        else:
            pass
            # Return a 'disabled account' error message
    else:
        pass
        # Return an 'invalid login' error message.
    print("Logged as user: "+str(user))
    return redirect(request.META['HTTP_REFERER'], context_instance=RequestContext(request))

def logouting(request):
    logout(request)
    # Redirect to a errors page.
    return redirect(request.META['HTTP_REFERER'], context_instance=RequestContext(request))


def register(request):
    # errors = []
    # if(request.POST.get('password','1') != request.POST.get('confirm_password','1')):
    #     errors.append('wrong_password')
    # if(request.POST.get('username', "field is empty") == "" or request.POST.get('email', "field is empty") == "" or request.POST.get('password',"field is empty") == ""):
    #     errors.append('empty_field')
    # if(len(errors) != 0):
    #     return render_to_response('profile/register.html', {'errors': errors}, RequestContext(request))
    # else:
    User.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    my_user = MyUser()
    my_user.user = user
    my_user.save()
    login(request, user)
    users_from_database = User.objects.all()
    return render_to_response('profile/account.html',{'users': users_from_database}, RequestContext(request))
# def register(request):
#     users_from_database = User.objects.all()
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             # send_mail(
#             #     cd['subject'],
#             #     cd['message'],
#             #     cd.get('email', 'noreply@example.com'),
#             #     ['siteowner@example.com'],
#             # )
#             return render_to_response('profile/account.html', {'users': users_from_database}, RequestContext(request))
#     else:
#         form = RegisterForm()
#     return render_to_response('profile/register.html', {'form': form},RequestContext(request))
@login_required
def account(request):
      if (request.POST):
        user = User.objects.get(id=request.user.id)
        my_user = MyUser.objects.get(user=user)
        if(request.POST['surname']):
            my_user.user.surname=request.POST['surname']
        # if(request.POST['birthday']):
        #     my_user.birthdate=request.POST['birthday']
        my_user.save()
        return render_to_response('profile/account.html',{'my_user': my_user}, RequestContext(request))
      else:
        user = User.objects.get(id=request.user.id)
        my_user = MyUser.objects.get(user=user)
        all_users = User.objects.all()
        return render_to_response('profile/account.html', {'my_user': my_user, 'all_users': all_users}, RequestContext(request))
