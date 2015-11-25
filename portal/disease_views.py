from django.shortcuts import render, render_to_response
from portal.models import *
from django.http import Http404
from django.template import RequestContext
import datetime
import mongoengine


def disease(request, disease_id):
    user = False
    try:
        if request.user.id:
            user_id = request.user.id
            user = MyUser.objects.get(user=User.objects.get(id=user_id))
        get_disease = Disease.objects.get(id=disease_id)
    except Disease.DoesNotExist:
        raise Http404("Poll does not exist")
    return render_to_response('disease/disease.html', {'disease': get_disease, 'myuser':user}, context_instance=RequestContext(request))


def like_comment(request):
    if request.POST:
        commentary= Comment.objects.get(id=request.POST['commentary_id'])
        commentary.point_comment+=1
        user = commentary.user
        user.point+=1
        user.save()
        commentary.save()

def add_specific_comment(request):
    category = CommentCategory.objects.get(name="Specialized")
    disease_to_comment = Disease.objects.get(id=request.POST['disease_id'])
    unit_duration_mapping={'D':"Dni","W":"Tygodni","M":"Miesięcy"}
    if request.POST:
        unit_dur = request.POST['unit_duration']
        value_dur = request.POST['value_duration']
        tips = request.POST['tips']
        age = request.POST['age']
        dsc = request.POST['description']
        new_comment = Comment(description=dsc, unit_duration=unit_dur, age=age, value_duration=str(value_dur), category=category, disease=disease_to_comment, tips=tips,point_comment=0.0)
        user_id = request.user.id
        new_comment.user = MyUser.objects.get(user=User.objects.get(id=user_id))
      #  new_comment.image = request.POST['image']
        new_comment.save()
        user = new_comment.user
        user.comments.append(new_comment)
        user.diseases.append(disease_to_comment)
        user.save()
        disease_to_comment.comments.append(new_comment)
        disease_to_comment.save()
    else:
        return render_to_response(request, 'base/index.html', {'all_news': None}, context_instance=RequestContext(request))
    #return render_to_response('disease/disease.html', {'disease': get_diseases}, context_instance=RequestContext(request))
    return render(request,"disease/disease.html", {'disease': disease_to_comment})


def add_question(request):
    category = CommentCategory.objects.get(name="Question")
    disease_to_comment = Disease.objects.get(id=request.POST['disease_id'])
    if request.POST:
        new_comment = Comment(category=category, description=request.POST['comment_to_add'])
        user_id = request.user.id
        new_comment.user = MyUser.objects.get(user=User.objects.get(id=user_id))
        new_comment.save()
        user = new_comment.user
        user.comments.append(new_comment)
        user.diseases.append(disease_to_comment)
        user.save()
        disease_to_comment.comments.append(new_comment)
        disease_to_comment.save()
    else:
        return render_to_response(request, 'base/index.html', {'all_news': None}, context_instance=RequestContext(request))
    #return render_to_response('disease/disease.html', {'disease': get_diseases}, context_instance=RequestContext(request))
    return render(request,"disease/disease.html", {'disease': disease_to_comment})


def add_comment(request):
    category = CommentCategory.objects.get(name="Disease")
    disease_to_comment = Disease.objects.get(id=request.POST['disease_id'])
    if request.POST:
        new_comment = Comment(category=category,description=request.POST['comment_to_add'])
        user_id = request.user.id
        new_comment.user = MyUser.objects.get(user=User.objects.get(id=user_id))
        new_comment.point_comment=0.0
        new_comment.save()
        user = new_comment.user
        user.comments.append(new_comment)
        user.diseases.append(disease_to_comment)
        user.save()
        disease_to_comment.comments.append(new_comment)
        disease_to_comment.save()
    else:
        return render_to_response(request, 'base/index.html', {'all_news': None}, context_instance=RequestContext(request))
    #return render_to_response('disease/disease.html', {'disease': get_diseases}, context_instance=RequestContext(request))
    return render(request,"disease/disease.html", {'disease': disease_to_comment})