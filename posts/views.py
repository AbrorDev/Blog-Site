from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Post, Comment
from .serializers import CategorySerializer, PostSerializer, UserSerializer, CommentSerializer
from .pagination import CustomPagination
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth.models import User

# Create your views here.

class CategoryViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    pagination_class = CustomPagination

class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get_context_data(self,*args, **kwargs):
        self.object.viewers.add(self.request.user)

class UserViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)