from django.shortcuts import render, render_to_response
from portal.models import *
from django.http import Http404
from django.template import RequestContext
import datetime
import mongoengine


def disease(request, disease_id):
    print('nothing!!!')
    try:
        get_disease = Disease.objects.get(id=disease_id)
    except Disease.DoesNotExist:
        raise Http404("Poll does not exist")
    return render_to_response('disease/disease.html', {'disease': get_disease}, context_instance=RequestContext(request))


def add_specific_comment(request):
    get_diseases = Disease.objects.all()
    if (request.POST):
        import pprint
        pprint.pprint(request.POST)
        time_dur=request.POST['unit_duration']+request.POST['value_duration']
        new_comment = Comment(date_publication=datetime.datetime.now(), description=request.POST['comment_to_add'], time_duration=time_dur)
        user_id = request.user.id
        print(request.user.id)
        new_comment.user = MyUser.objects.get(user=User.objects.get(id=user_id))
        print(new_comment.user)
        new_comment.save()
        disease_to_comment = Disease.objects.get(id=request.POST['disease_id'])
        disease_to_comment.comments.append(new_comment)
        disease_to_comment.save()
    else:
        return render_to_response(request, 'base/index.html', {'all_news': None}, context_instance=RequestContext(request))
    #return render_to_response('disease/disease.html', {'disease': get_diseases}, context_instance=RequestContext(request))
    return render(request,"disease/disease.html", {'disease': get_diseases})


def add_question(request):
    get_diseases = Disease.objects.all()
    if (request.POST):
        import pprint
        pprint.pprint(request.POST)
        new_comment = Comment(date_publication=datetime.datetime.now(), description=request.POST['comment_to_add'])
        user_id = request.user.id
        print(request.user.id)
        new_comment.user = MyUser.objects.get(user=User.objects.get(id=user_id))
        print(new_comment.user)
        new_comment.save()
        disease_to_comment = Disease.objects.get(id=request.POST['disease_id'])
        disease_to_comment.comments.append(new_comment)
        disease_to_comment.save()
    else:
        return render_to_response(request, 'base/index.html', {'all_news': None}, context_instance=RequestContext(request))
    #return render_to_response('disease/disease.html', {'disease': get_diseases}, context_instance=RequestContext(request))
    return render(request,"disease/disease.html", {'disease': get_diseases})


def add_comment(request):
    get_diseases = Disease.objects.all()
    if (request.POST):
        import pprint
        pprint.pprint(request.POST)
        new_comment = Comment(date_publication=datetime.datetime.now(), description=request.POST['comment_to_add'])
        user_id = request.user.id
        print(request.user.id)
        new_comment.user = MyUser.objects.get(user=User.objects.get(id=user_id))
        print(new_comment.user)
        new_comment.save()
        disease_to_comment = Disease.objects.get(id=request.POST['disease_id'])
        disease_to_comment.comments.append(new_comment)
        disease_to_comment.save()
    else:
        return render_to_response(request, 'base/index.html', {'all_news': None}, context_instance=RequestContext(request))
    #return render_to_response('disease/disease.html', {'disease': get_diseases}, context_instance=RequestContext(request))
    return render(request,"disease/disease.html", {'disease': get_diseases})