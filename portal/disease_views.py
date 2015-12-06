from django.shortcuts import render, render_to_response,HttpResponse
from portal.models import *
from django.http import Http404
from django.template import RequestContext
import datetime
import mongoengine
import json

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
        commentary.point_comment+=2
        user = commentary.user
        user.point+=2
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
        user.comment_count+=6
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
        new_comment = Comment(category=category,description=request.POST['comment_to_add'],point_comment=0.0)
        user_id = request.user.id
        new_comment.user = MyUser.objects.get(user=User.objects.get(id=user_id))
        new_comment.save()
        user = new_comment.user
        user.comment_count+=2
        user.comments.append(new_comment)
        user.diseases.append(disease_to_comment)
        user.save()
        disease_to_comment.comments.append(new_comment)
        disease_to_comment.save()
    else:
        return render_to_response(request, 'base/index.html', {'all_news': None}, context_instance=RequestContext(request))
    #return render_to_response('disease/disease.html', {'disease': get_diseases}, context_instance=RequestContext(request))
    return render(request,"disease/disease.html", {'disease': disease_to_comment})


def add_disease(request):
    #add_public_terms()
    if request.POST:
        if 'disease_name' in request.POST:
            new_disease = Disease(name=request.POST['disease_name'], description=request.POST['description'], cure=request.POST['cure'])
            my_user= MyUser.objects.get(user=User.objects.get(id=request.user.id))
            new_disease.founder = my_user
            new_disease.key_words =request.POST['key_words'].split()
            new_disease.save()
            my_user.diseases.append(new_disease)
            my_user.comment_count+=2
            my_user.disease_added_count+=2
            my_user.save()
        # elif 'friend' in request.POST:

        return render(request,"disease/disease.html", {'disease': new_disease})
    else:
        try:
            discussions = Disease.objects.all().order_by('-date_publication')[:3]
        except Disease.DoesNotExist:
            raise Http404("Poll does not exist")
        return render_to_response('disease/add_disease.html', {'discussion_list':discussions}, context_instance=RequestContext(request))

def add_article(request):
    #add_public_terms()
    if request.POST:
        if 'disease_name' in request.POST:
            disease=Disease.objects.get(name=request.POST['disease'])
            article = Article(name=request.POST['disease_name'], description=request.POST['description'],disease=disease )
            my_user= MyUser.objects.get(user=User.objects.get(id=request.user.id))
            article.founder = my_user
            article.key_words =request.POST['key_words'].split()
            article.save()
            my_user.articles.append(article)
            my_user.article_added_count=2
            my_user.point=20
            my_user.save()
            disease.articles.append(article)
            disease.save()
        # elif 'friend' in request.POST:

        return render(request,"disease/article.html", {'article': article})
    else:
        try:
            discussions = Disease.objects.all().order_by('-date_publication')[:3]
        except Disease.DoesNotExist:
            raise Http404("Poll does not exist")
        return render_to_response('disease/add_article.html', {'discussion_list':discussions}, context_instance=RequestContext(request))

def articles(request):
    try:
        articles_list = Article.objects.all().order_by('-date_publication')[:3]
        articles_selected = Article.objects.all().order_by('-date_publication')[:3]
        if request.POST:
            articles_selected=Article.objects.filter(name__icontains=request.POST['name_searchbox'])

    except Article.DoesNotExist:
        raise Http404("Nie można uzyskać artykułów")
    return render_to_response('disease/articles.html', {'articles': articles_list,'articles_selected': articles_selected}, context_instance=RequestContext(request))


def article(request, article_id):
    try:
        get_article = Article.objects.get(id=article_id)
        if request.POST:
            if "article" in request.POST:
                get_article.point+=1
                get_article.save()
    except Disease.DoesNotExist:
        raise Http404("Poll does not exist")
    return render_to_response('disease/article.html', {'article': get_article}, context_instance=RequestContext(request))

def get_article(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        print("loking for "+q)
        diseases = Article.objects.filter(name__icontains=q)[:20]

        results = []
        for disease in diseases:
            disease_json = {}
            disease_json['id'] = 1
            disease_json['label'] = disease.name
            disease_json['value'] = disease.name
            print(disease_json)
            results.append(disease_json)
        results=json.dumps(results)
        print("my data: "+str(results))
        mimetype = 'application/json'
        print(results)
        return HttpResponse(results, mimetype)
    else:
        data = Disease.objects.all()[:10]
    print("**************************")
    mimetype = 'application/json'
    print(data)
    return HttpResponse(data, mimetype)

