# blog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserCreateView

router = DefaultRouter()
router.register(r'', UserCreateView, basename='post')

urlpatterns = [
    path('', include(router.urls)),
]
