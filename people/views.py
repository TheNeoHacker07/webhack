from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,CreateAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrReadOnly
from .serializer import PeopleTypeSerializer
from .models import PeopleType



class PeopleList(ListAPIView):
    queryset=PeopleType.objects.all()
    serializer_class=PeopleTypeSerializer
    permission_class=(AllowAny)
    filter_backends=(SearchFilter,DjangoFilterBackend)
    search_fields=('first_name','second_name','email')

class PersonRetriev(RetrieveAPIView):
    queryset=PeopleType.objects.all()
    serializer_class=PeopleTypeSerializer
    lookup_field='id'
    permission_classes=[AllowAny]
    filter_backends=(SearchFilter,DjangoFilterBackend)
    search_fields=('first_name','second_name','email')


class PersonCreate(ListCreateAPIView):
    queryset=PeopleType.objects.all()
    serializer_class=PeopleTypeSerializer    
    


class PersonDelete(DestroyAPIView):
    queryset=PeopleType.objects.all()
    serializer_class=PeopleTypeSerializer
    lookup_field='id'
    permission_classes=(IsAuthenticated)

class PersonUpdate(UpdateAPIView):
    queryset=PeopleType.objects.all()
    serializer_class=PeopleTypeSerializer
    lookup_field='id'
    permission_classes=(IsOwnerOrReadOnly)

# Create your views here.
