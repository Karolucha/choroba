from django.shortcuts import render, render_to_response
from portal.models import *
from django.http import Http404
from django.template import RequestContext
import datetime
import mongoengine

mongoengine.connect('misiowa')


def index(request):
    return render(request, 'base/index.html', {'all_news': None}, context_instance=RequestContext(request))


def search_disease(request):
    # initializer()

    if (request.POST):
        #print(request.POST.get('last_name_searchbox'))
        diseases = Disease.objects.filter(name__startswith=request.POST.get('last_name_searchbox'))
        #print(diseases)
        #diseases = Disease.objects.all()
    else:
        diseases = Disease.objects.all()

    return render(request, 'disease/search.html', {'diseases_list': diseases}, context_instance=RequestContext(request))


def disease(request, disease_id):
    try:
        get_disease = Disease.objects.get(id=disease_id)
    except Disease.DoesNotExist:
        raise Http404("Poll does not exist")
    return render_to_response('disease/disease.html', {'disease': get_disease}, context_instance=RequestContext(request))


def result_disease(request, disease_name):
    if (request.POST):
        get_disease = Disease.objects.filter(name__startswith=request.POST.get('last_name_searchbox', 'alergia'))
    else:
        return render_to_response(request, 'base/index.html', {'all_news': None}, context_instance=RequestContext(request))
    return render_to_response('disease/disease.html', {'disease': get_disease}, context_instance=RequestContext(request))


def add_comment(request, comment_dict):
    get_diseases = Disease.objects.all()
    if (request.POST):
        new_comment = Comment(date_publication=datetime.datetime.now(), description=comment_dict.get('description', ''))
        new_comment.user = MyUser.objects.get(id=comment_dict.get('user_id', ''))
        new_comment.save()
        disease_to_comment = Disease.objects.get(id=comment_dict.get('disease_id', ''))
        disease_to_comment.comments.append(new_comment)
        disease_to_comment.save()
    else:
        return render_to_response(request, 'base/index.html', {'all_news': None}, context_instance=RequestContext(request))
    return render_to_response('disease/disease.html', {'disease': get_diseases}, context_instance=RequestContext(request))


def articles(request):
    try:
        articles_list = Article.objects.all()
    except Disease.DoesNotExist:
        raise Http404("Poll does not exist")
    return render_to_response('disease/articles.html', {'articles': articles_list}, context_instance=RequestContext(request))


def article(request, article_id):
    try:
        get_article = Article.objects.get(id=article_id)
    except Disease.DoesNotExist:
        raise Http404("Poll does not exist")
    return render_to_response('disease/article.html', {'article': get_article}, context_instance=RequestContext(request))


def initializer():
    # user1 = MyUser(username="lalka", password="lala99pysia", sex="K", note="jestem zadowolona", email="xxx@pl.pl").save()
    user1 = MyUser.objects.get(username="lalka")
    user2 = MyUser.objects.get(username="Ewka")
    # user2 = MyUser(username="Ewka", password="123456", sex="K", note="jestem ewka marchewka", email="karolka_her@o2.pl").save()
    commentary_creator = Comment(date_publication=datetime.datetime.now(), description="bylo cudownie")
    commentary_creator.user = user1
    commentary_creator.save()
    commentary_creator2 = Comment(date_publication=datetime.datetime.now(),
                                  description="jestem teraz szczupła więc dobrze mi zrobiło")
    commentary_creator.user = user2
    commentary_creator2.save()
    commentary_creator3 = Comment(date_publication=datetime.datetime.now(), description="bawiłam się dobrze")
    commentary_creator.user = user1
    commentary_creator3.save()
    article_creator = Article(date_publication=datetime.datetime.now(), name='Kurowanie gdy ...',
                              description='\rHerbatka pyszna i cytrynka i brokul wymieszalam.\n\rwspaniale smakowalo')
    article_creator.user = user1
    article_creator.save()
    article_creator2 = Article(date_publication=datetime.datetime.now(), name='Lasciami ...',
                               description='\rJestem i cytrynka i brokul wymieszalam.\n\rwspaniale smakowalo')
    article_creator.user = user2
    article_creator2.save()
    diseases_creator = Disease(name='alergia: roztocze', description='kazdy na to cierpi', cure='ziolowe napary')
    diseases_creator.comments = [commentary_creator, commentary_creator2, commentary_creator3]
    diseases_creator.articles = [article_creator, article_creator2]
    diseases_creator.save()
    diseases_creator = Disease(name='piękna cera', description='zdrowe jedzenie')
    diseases_creator.comments = [commentary_creator, commentary_creator2, commentary_creator3]
    diseases_creator.articles = [article_creator, article_creator2]
    diseases_creator.save()
    diseases_creator = Disease(name='szczupła sylwetka', description='ruch i zdrowie')
    diseases_creator.comments = [commentary_creator, commentary_creator2, commentary_creator3]
    diseases_creator.articles = [article_creator, article_creator2]
    diseases_creator.save()
