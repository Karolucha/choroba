from django.shortcuts import render, render_to_response,HttpResponse
from portal.models import *
from django.http import Http404
from django.template import RequestContext
import datetime
import mongoengine
from portal.disease_views import *
from portal.discussion_view import *
from mongoengine.django.auth import *
from django.views.decorators.csrf import csrf_protect
mongoengine.connect('misiowa')
import json

def index(request):
    return render(request, 'base/index.html', {'all_news': None}, context_instance=RequestContext(request))


def search_disease(request):
  #  initializer()
  #  add_perms()

    if (request.POST):
        #print(request.POST.get('last_name_searchbox'))
        diseases = Disease.objects.filter(name__icontains=request.POST.get('last_name_searchbox'))
        #print(diseases)
        #diseases = Disease.objects.all()
    else:
        top_comment = Comment.objects.all().order_by('-date_publication')[:10]
        #for disease in Disease.objects.all():
        #    for comment in disease.comments:
        #        if com`m
        diseases = Disease.objects.all().order_by('-id')[:10]
    print(diseases)
    return render(request, 'disease/search.html', {'diseases_list': diseases}, context_instance=RequestContext(request))


def result_disease(request, disease_name):
    if (request.POST):
        get_disease = Disease.objects.filter(name__startswith=request.POST.get('last_name_searchbox', 'alergia'))
    else:
        return render_to_response(request, 'base/index.html', {'all_news': None}, context_instance=RequestContext(request))
    return render_to_response('disease/disease.html', {'disease': get_disease}, context_instance=RequestContext(request))


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


def get_cycki(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        print("loking for "+q)
        cyckis = Disease.objects.filter(name__icontains=q)[:20]

        results = []
        for cycki in cyckis:
            cycki_json = {}
            cycki_json['id'] = 1
            cycki_json['label'] = cycki.name
            cycki_json['value'] = cycki.name
            print(cycki_json)
            results.append(cycki_json)
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


def add_perms():

    # perm = Permission()
    # perm.codename='adder_disease'
    # perm.name='Lekarz dyżurujący'
    # perm.save()
    # perm = Permission()
    # perm.codename='adder_article'
    # perm.name='Recepcjonista'
    # perm.save()
    # perm = Permission()
    # perm.codename='admin'
    # perm.name='Ordynator'
    # perm.save()
    # perm = Permission()
    #Permission.objects.create(codename='cleaner', name='Położna')
    #Permission.objects.create(codename='adder_disease', name='Lekarz dyżurujący')
    #Permission.objects.create(codename='adder_article', name='Pacjent Nowak')
    #Permission.objects.create(codename='admin', name='Ordynator')
    user1 = MyUser.objects.get(user=User.objects.get(username="tomek"))
    user1.user.user_permissions.append(Permission.get(codename="adder_disease"))
    user1.user.user_permissions.append(Permission.get(codename="adder_article"))
    user1.save()
def initializer():
    # user1 = MyUser(username="lalka", password="lala99pysia", sex="K", note="jestem zadowolona", email="xxx@pl.pl").save()
    #role1 = UserRoles(name="Pacjent", description="Jest to zwykly zarejestrowany użytkownik")
    # role2 = UserRoles(name="Siostra", description="Użytkownik może dodawać choroby")
    # role3 = UserRoles(name="Lekarz dyżurny", description="Użytkownik może dodawać artykuły")
    # role4 = UserRoles(name="Ordynator", description="Użytkownik może zgłaszać nieprawidłowe komentarze")
    # role2.save()
    # role3.save()
    # role4.save()

    role2=UserRoles.objects.get(name="Siostra")
    role3=UserRoles.objects.get(name="Lekarz dyżurny")
    role4=UserRoles.objects.get(name="Ordynator")


    # user1 = MyUser.objects.get(user=User.objects.get(username="tomek"))
    # user2 = MyUser.objects.get(user=User.objects.get(username="Karolina"))
    # user3 = MyUser.objects.get(user=User.objects.get(username="Ewka"))
    # user4 = MyUser.objects.get(user=User.objects.get(username="lalka"))
    user1 = MyUser(user=User.objects.get(username="tomek"),note="sympatyczny chłopak", roles = [role2,role3, role4]).save()
    user2 = MyUser(user=User.objects.get(username="Karolina"),roles = [role2,role3, role4]).save()
    user3 = MyUser(user=User.objects.get(username="Ewka"), roles = [role2,role3]).save()
    user4 = MyUser(user=User.objects.get(username="lalka")).save()
    # user1.friends =[user2]
    # user2.friends =[user1]
    # user1.save()
    # user2.save()
    # user3.save()
    # user4.save()
    # user2 = MyUser(username="Ewka", password="123456", sex="K", note="jestem ewka marchewka", email="karolka_her@o2.pl").save()

    cat1 = CommentCategory(name='Disease').save()
    cat2 = CommentCategory(name='Question').save()
    cat3 = CommentCategory(name='Discussion').save()
    cat4 = CommentCategory(name='Specialized').save()


    commentary_creator = Comment(date_publication=datetime.datetime.now(), description="bylo cudownie", category=cat1)
    commentary_creator.user = user1
    commentary_creator.save()
    user1.comments=[commentary_creator]
    commentary_creator2 = Comment(date_publication=datetime.datetime.now(),                                  description="jestem teraz szczupła więc dobrze mi zrobiło")
    commentary_creator.user = user2
    commentary_creator2.save()
    user2.comments=[commentary_creator2]
    commentary_creator3 = Comment(date_publication=datetime.datetime.now(), description="bawiłam się dobrze")
    commentary_creator.user = user3
    commentary_creator3.save()
    user3.comments=[commentary_creator3]
    article_creator = Article(date_publication=datetime.datetime.now(), name='Kurowanie gdy ...',
                              description='\rHerbatka pyszna i cytrynka i brokul wymieszalam.\n\rwspaniale smakowalo',founder=user1)
    article_creator.user = user1
    article_creator.save()
    user1.articles=[article_creator]
    article_creator2 = Article(date_publication=datetime.datetime.now(), name='Lasciami ...',
                               description='\rJestem i cytrynka i brokul wymieszalam.\n\rwspaniale smakowalo',founder=user2)
    article_creator2.user = user2
    article_creator2.save()
    user1.articles=[article_creator2]
    diseases_creator = Disease(name='alergia: roztocze', description='kazdy na to cierpi', cure='ziolowe napary', founder=user1)
    diseases_creator.comments = [commentary_creator, commentary_creator2, commentary_creator3]
    diseases_creator.articles = [article_creator, article_creator2]
    diseases_creator.save()
    user1.diseases=[diseases_creator]
    diseases_creator = Disease(name='piękna cera', description='zdrowe jedzenie',founder=user2)
    diseases_creator.comments = [commentary_creator, commentary_creator2, commentary_creator3]
    diseases_creator.articles = [article_creator, article_creator2]
    diseases_creator.save()
    user2.diseases=[diseases_creator]
    diseases_creator = Disease(name='szczupła sylwetka', description='ruch i zdrowie',founder=user3)
    diseases_creator.comments = [commentary_creator, commentary_creator2, commentary_creator3]
    diseases_creator.articles = [article_creator, article_creator2]
    diseases_creator.save()
    user3.diseases=[diseases_creator]

    user1.save()
    user2.save()
    user3.save()
    user4.save()