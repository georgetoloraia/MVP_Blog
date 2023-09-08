# blog/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView, UserLoginView #ProfileView, SetBioView

router = DefaultRouter()
router.register(r'registration', UserRegistrationView, basename='registration')
router.register(r'login', UserLoginView, basename='login')
#router.register(r'profile', ProfileView, basename='profile')
#router.register(r'bio', SetBioView, basename='bio')

urlpatterns = [
    path('', include(router.urls)),
]
