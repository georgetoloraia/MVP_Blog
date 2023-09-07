# blog/views.py
from rest_framework import generics, viewsets
from .models import Post
from .serializers import PostSerializer

class PostListCreateView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
