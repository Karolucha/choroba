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
    diseases = Disease.objects.all().order_by('-date_publication')[:3]
    diseases_ALL = Disease.objects.order_by('-date_publication')[:10]
    return render(request, 'disease/search.html', {'diseases_list': diseases, 'diseases_all': diseases_ALL}, context_instance=RequestContext(request))


def search_disease(request):
  #  initializer()

    if (request.POST):
        diseases = Disease.objects.filter(name__icontains=request.POST.get('last_name_searchbox'))
    else:
        top_comment = Comment.objects.all().order_by('-date_publication')[:10]
        #for disease in Disease.objects.all():
        #    for comment in disease.comments:
        #        if com`m
        diseases = Disease.objects.all().order_by('-id')[:10]
    print(diseases)
    diseases_ALL = Disease.objects.order_by('-date_publication')
    diseases = Disease.objects.all().order_by('-date_publication')[:3]
    return render(request, 'disease/search.html', {'diseases_list': diseases, 'diseases_all': diseases_ALL}, context_instance=RequestContext(request))


def hots(request):
    if request.POST:
        if 'question' in request.POST:
            user = MyUser.objects.get(user=User.objects.get(id=request.user.id))
            question = Question(question=request.POST['question'], user=user)
            question.save()
           # question = Question.objects.all()[0]
            user.questions.append(question)
            user.save()
            request.POST={}
        if 'answer' in request.POST:
            specialist = Specialist.objects.get(user=User.objects.get(id=request.user.id))
            question = Question.objects.get(id=request.POST['question'])
            question.specialist=specialist
            question.answer=request.POST['answer']
            date_answer=datetime.datetime.now
            if 'disease' in request.POST:
                question.disease = Disease.objects.get(name=request.POST['disease'])
            question.save()
    questions = Question.objects.all().order_by('-date_publication')[:3]
    # questions_answered= Question.get_answered()
    # print(questions_answered)
    return render(request, 'disease/hots.html', {'questions_list': questions}, context_instance=RequestContext(request))


def question(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.POST:
        if 'answer' in request.POST:
            specialist = Specialist.objects.get(user=User.objects.get(id=request.user.id))
            question.specialist = specialist
            question.answer = request.POST['answer']
            question.date_answer = datetime.datetime.now
        if 'disease' in request.POST:
            question.disease = Disease.objects.get(name=request.POST['disease'])
        question.save()
    return render(request, 'disease/question.html', {'question': question}, context_instance=RequestContext(request))

def api_question(request, question_id):
    '''
    Prześlij mu id question
     -post pod kluczem 'question' tekst pytania, question_id daj sztucznie np 0
     -get po prostu id zadanego pytania, przechowuj id zwrócone w json po zadaniu pytania aby wysyłać
    '''
    results = []
    mimetype = 'application/json'

    if question_id!=0:
        question = Question.objects.get(id=question_id)
        results.append(question.to_json())

    if request.POST:
        question = Question(question=request.POST['question'])
        #question.save()
        results.append(question.to_json())
        results=json.dumps(results)

    results=json.dumps(results)
    return HttpResponse(results, mimetype)



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

def result_disease(request, disease_name):
    if request.POST:
        get_disease = Disease.objects.filter(name__startswith=request.POST.get('last_name_searchbox', 'alergia'))
    else:
        return render_to_response(request, 'base/index.html', {'all_news': None}, context_instance=RequestContext(request))
    return render_to_response('disease/disease.html', {'disease': get_disease}, context_instance=RequestContext(request))



def get_disease(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        print("loking for "+q)
        diseases = Disease.objects.filter(name__icontains=q)[:20]

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