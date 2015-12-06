__author__ = 'karolinka'
from rest_framework.response import Response
from portal.models import Comment, CommentSerialize
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', 'POST'])
def comments_list(request):
    """
    List all comments, NYI or create a new comment.
    """
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerialize(comments, many=True)
        return Response(serializer.data)

    # NYI
    #elif request.method == 'POST':
    #    serializer = CommentSerialize(data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)