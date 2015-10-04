
from django.shortcuts import render_to_response, redirect
from portal.models import *
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
import mongoengine
#mongoengine.connect('misiowa')
from mongoengine.django.auth import User

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


def register(request, problems=0):
    if(problems==0):
        return render_to_response('register.html', RequestContext(request))
    errors = []
    if(request.POST.get('password', 1) != request.POST.get('confirm_password', 2)):
        errors.append('wrong_password')
    if(request.POST.get('username', "field is empty") == "" or request.POST.get('email', "field is empty") == "" or request.POST.get('password',"field is empty") == ""):
        errors.append('empty_field')
    if(len(errors) != 0):
        return render_to_response('register.html', {'errors': errors}, RequestContext(request))  
    else:   
        User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])     
        user=authenticate(username=request.POST['username'], password=request.POST['password'])
        login(request, user)
        return render_to_response('index.html', RequestContext(request))


def account(request):
    # example_insert_user()
    try:
        users_from_database = User.objects.all()
    except users_from_database.DoesNotExist:
        raise Http404

    return render_to_response('profile/account.html', {'users': users_from_database}, RequestContext(request))
