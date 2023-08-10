from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class TaskSerialiser(serializers.ModelSerializer):
    # dueDate = serializers.DateTimeField(read_only = True)
    id = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField(source="creator.username")
    dueDate = serializers.DateTimeField()
    class Meta:
        model = models.Tasks
        fields = ['title', 'status', 'priority', 'id', 'username', 'dueDate']
    
    def validate(self, attrs):
        return super().validate(attrs)
    
# class UserSerializer(serializers.ModelSerializer):
#     title = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Tasks.objects.all())
#     class Meta:
#         model = User
#         fields = ['title', 'id', 'username']