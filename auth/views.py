from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .serializers import UserRegisterSerializer
from rest_framework import response
from django.contrib.auth.models import User
# Create your views here.


class UserRegister(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (permissions.AllowAny,)