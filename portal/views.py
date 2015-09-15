from django.shortcuts import render, render_to_response
from portal.models import *
from django.http import Http404
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
    diseases_creator =Disease(name='alergia: roztocze', description='kazdy na to cierpi')
    diseases_creator.save()
    diseases_creator =Disease(name='piękna cera', description='zdrowe jedzenie')
    diseases_creator.save()
    diseases_creator =Disease(name='szczupła sylwetka', description='ruch i zdrowie')
    diseases_creator.save()


def search_disease(request):

    diseases = Disease.objects.all()
    return render(request, 'disease/search.html', {'diseases_list': diseases})

def disease(request, disease_id):
    try:
        get_disease = Disease.objects.get(id=disease_id)
    except Disease.DoesNotExist:
        raise Http404("Poll does not exist")
    return render_to_response('disease/disease.html', {'disease': get_disease})
