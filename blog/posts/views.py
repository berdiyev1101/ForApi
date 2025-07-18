from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import PostSerializers,UserSerializer
from posts.models import Post
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAuthorOrReadOnly
# Create your views here.

class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
