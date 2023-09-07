from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User #get_user_model
from .models import CustomUser
from .serializers import CustomUserSerializer

user = User #get_user_model()

class UserCreateView(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
