from django.shortcuts import render

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Comment
from .serializer import CommentSerializer
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from rest_framework.filters import SearchFilter

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrReadOnly
from people.models import PeopleType 
from .models import Comment,Like

class CommentViewSet(ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    filter_backends=(SearchFilter,DjangoFilterBackend)
    search_fields=('author','text')


    def get_permissions(self):
        if self.action in ['list','retrieve']:
            self.permission_classes=[AllowAny]
        elif self.action in ['create']:
            self.permission_classes=[IsAuthenticated]
        elif self.action in ['update','partial_update','destroy']:
            self.permission_classes=[IsOwnerOrReadOnly]

        return [permission() for permission in self.permission_classes]







from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    current_user = request.user
    return HttpResponse(f"Hello, {current_user.email}!")




@api_view(['POST'])
def like_handler(request,id):
    if not request.user.is_authenticated:
        return Response(401)
    post=get_object_or_404(PeopleType,id=id)
    if Like.objects.filter(user=request.user,post=post).exists():
        Like.objects.filter(user=request.user,post=post).delete()
    else:
        Like.objects.create(user=request.user,post=post)
    return Response(201)



# Create your views here.
