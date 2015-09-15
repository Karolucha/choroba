from django.shortcuts import render, render_to_response
from portal.models import *
from django.http import Http404
import datetime
# Create your views here.
import mongoengine
mongoengine.connect('misiowa')
def index(request):
    #return render(request, 'base/index.html')

    # poll = Poll.objects(question__contains="What").first()
    # choice = Choice(choice_text="I'm at DjangoCon.fi", votes=23)
    # print("Poll: "+str(poll))
    # poll.choices.append(choice)
    # poll.save()
    return render(request, 'base/index.html', {'all_news': None})



def initializer():
    user1 = MyUser(username="lalka", password="lala99pysia", sex="K", note="jestem zadowolona", email="xxx@pl.pl")
    user2 = MyUser(username="Ewka", password="123456", sex="K", note="jestem ewka marchewka")
    user1.save()
    commentary_creator = Comment(date_publication=datetime.datetime.now(), description="bylo cudownie")
    commentary_creator.user = user1
    commentary_creator.save()
    # commentary_creator2 = Comment(user=user2, date_publication=datetime.datetime.now(), description="jestem teraz szczupła więc dobrze mi zrobiło")
    # commentary_creator2.save()
    # commentary_creator3 = Comment(user=user1, date_publication=datetime.datetime.now(), description="bawiłam się dobrze")
    # commentary_creator3.save()
    # article_creator = Article(user=user1, date_publication=datetime.datetime.now(), name='Kurowanie gdy ...', description='\rHerbatka pyszna i cytrynka i brokul wymieszalam.\n\rwspaniale smakowalo')
    # article_creator.save()
    # article_creator2 = Article(user=user2, date_publication=datetime.datetime.now(), name='Lasciami ...', description='\rJestem i cytrynka i brokul wymieszalam.\n\rwspaniale smakowalo')
    # article_creator2.save()
    # diseases_creator = Disease(name='alergia: roztocze', description='kazdy na to cierpi', cure='ziolowe napary', comments=[commentary_creator, commentary_creator2, commentary_creator3], articles=[article_creator, article_creator2])
    # diseases_creator.save()
    # diseases_creator = Disease(name='piękna cera', description='zdrowe jedzenie', comments=[commentary_creator, commentary_creator2, commentary_creator3], articles=[article_creator, article_creator2])
    # diseases_creator.save()
    # diseases_creator = Disease(name='szczupła sylwetka', description='ruch i zdrowie', comments=[commentary_creator, commentary_creator2, commentary_creator3], articles=[article_creator, article_creator2])
    # diseases_creator.save()

def search_disease(request):
    initializer()
    diseases = Disease.objects.all()
    return render(request, 'disease/search.html', {'diseases_list': diseases})

def disease(request, disease_id):
    try:
        get_disease = Disease.objects.get(id=disease_id)
    except Disease.DoesNotExist:
        raise Http404("Poll does not exist")
    return render_to_response('disease/disease.html', {'disease': get_disease})
