from django.shortcuts import render
from rest_framework.generics import ListAPIView
from library.models import *
from .serializers import *
# Create your views here.
class BookAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

