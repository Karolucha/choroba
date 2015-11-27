from django.shortcuts import render, render_to_response
from portal.models import *
from django.http import Http404
from django.template import RequestContext
import datetime
import mongoengine


def discussion(request, discussion_id):
    # try:
    get_discussion = Discussion.objects.get(id=discussion_id)
    message=""
    if request.POST:
        if 'comment_to_add' in request.POST:
            print('dalej tu')
            new_comment = Comment(category=CommentCategory.objects.get(name="Discussion"), description=request.POST['comment_to_add'],point_comment=0.0)
            new_comment.user = MyUser.objects.get(user=User.objects.get(id=request.user.id))
            new_comment.save()
            get_discussion.comments.append(new_comment)
            get_discussion.save()
            request.POST=None
        elif 'friend' in request.POST:
            my_user= MyUser.objects.get(user=User.objects.get(id=request.POST['friend']))
            invitation= Invitation(inviting=request.user, invited=my_user).save()
            message="Pomyslnie wysłano zaproszenie"
    return render_to_response('discussion/discussion.html', {'discussion': get_discussion,'message_success':message, }, context_instance=RequestContext(request))

def add_discussion(request):
    #add_public_terms()
    if request.POST:
        if 'discussion_name' in request.POST:
            new_discussion = Discussion(name=request.POST['discussion_name'], description=request.POST['description'])
            new_discussion.public_term = PublicTerms.objects.get(code=request.POST['term'])
            my_user= MyUser.objects.get(user=User.objects.get(id=request.user.id))
            new_discussion.founder = my_user
            new_discussion.disease =Disease.objects.get(name=request.POST['disease'])
            new_discussion.key_words =request.POST['key_words'].split()
            new_discussion.save()
            my_user.discussions.append(new_discussion)
            my_user.discussion_added_count+=1
            my_user.save()
        # elif 'friend' in request.POST:

        return render_to_response('discussion/discussion.html', {'discussion':new_discussion}, context_instance=RequestContext(request))
    else:
        try:
            get_terms = PublicTerms.objects.all()
            discussions = Discussion.objects.all()
        except Disease.DoesNotExist:
            raise Http404("Poll does not exist")
        return render_to_response('discussion/add_discussion.html', {'public_terms': get_terms, 'discussion_list':discussions}, context_instance=RequestContext(request))


def add_comment_discussion(request):
    category = CommentCategory.objects.get(name="Discussion")
    discussion_to_comment = Discussion.objects.get(id=request.POST['discussion_id'])
    if request.POST:
        new_comment = Comment(category=category, description=request.POST['comment_to_add'],point_comment=0.0)
        new_comment.user = MyUser.objects.get(user=User.objects.get(id=request.user.id))
        new_comment.save()
        discussion_to_comment.comments.append(new_comment)
        discussion_to_comment.save()
    else:
        return render_to_response(request, 'base/index.html', {'all_news': None}, context_instance=RequestContext(request))
    #return render_to_response('disease/disease.html', {'disease': get_diseases}, context_instance=RequestContext(request))
    return render(request,"discussion/discussion.html", {'discussion': discussion_to_comment})





def add_public_terms():
  #  terms = PublicTerms(name="Każdy użytkownik może dodawać i czytać komentarze", code="A").save()
 #   terms = PublicTerms(name="Każdy użytkownik może czytać komentarze w dyskusji, tylko zaproszony może dodawać nowe", code="ARI").save()
   # terms = PublicTerms(name="Każdy użytkownik może czytać komentarze w dyskusji, tylko zaproszeni i znajomi mogą dodawać nowe", code="ARF").save()
  #  terms = PublicTerms(name="Tylko zaproszony do dyskusji może dodawać komentarze", code="I").save()
    terms = PublicTerms(name="Tylko zaproszeni i znajomi mogą dodawać komentarze", code="F").save()