# blog/urls.py
from django.urls import path, include
from .views import PostListCreateView, PostDetailView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostListCreateView, basename='post')
router.register(r'posts/<int:pk>', PostDetailView, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]
