from django.shortcuts import render
from portal.models import Poll, Choice
# Create your views here.
import mongoengine
mongoengine.connect('misiowa')
def index(request):
    #return render(request, 'base/index.html')

    poll = Poll.objects(question__contains="What").first()
    choice = Choice(choice_text="I'm at DjangoCon.fi", votes=23)
    print("Poll: "+str(poll))
    poll.choices.append(choice)
    poll.save()
    return render(request, 'base/index.html', {'all_news': None})
