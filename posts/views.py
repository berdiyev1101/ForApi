from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import PostSerializers
from posts.models import Post
# Create your views here.

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers