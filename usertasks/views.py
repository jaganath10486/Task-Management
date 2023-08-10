from django.shortcuts import render
from rest_framework import generics
from rest_framework import response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth.models import User
from .serializers import TaskSerialiser
from .models import Tasks
from .permissions import IsOwner
from django_filters import rest_framework as filter
from rest_framework import filters

class TaskView(generics.ListCreateAPIView):
    serializer_class = TaskSerialiser
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filter.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, )
    filterset_fields = ['status', 'priority']
    search_fields = ['title']
    ordering_fields=['status']
    def perform_create(self, serializer):
        serializer.save(creator = self.request.user)
    def get_queryset(self):
        return Tasks.objects.filter(creator = self.request.user)
   


class TaskIdView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerialiser
    # lookup_field = 'pk'
    queryset = Tasks.objects.all()
    permission_classes = (permissions.IsAuthenticated,IsOwner, )
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
class UserView(generics.ListAPIView):
    queryset = User.objects.all()