from django.shortcuts import render
from portal.models import Poll, Choice
# Create your views here.


def index(request):
    poll = Poll.objects(question__contains="What").first()
    choice = Choice(choice_text="I'm at DjangoCon.fi", votes=23)
    poll.choices.append(choice)
    poll.save()
    return render(request, 'base/index.html', {'all_news': None})
