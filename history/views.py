from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView


from .models import  History
from .serializer import HistorySerializer

class ListHistory(ListAPIView):
    queryset=History.objects.all()
    serializer_class=HistorySerializer


class RetrieveHistory(RetrieveAPIView):
    queryset=History.objects.all()
    serializer_class=HistorySerializer
    lookup_field='id'




# Create your views here.
