from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length = 10)
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
    def validate(self, attrs):
        if(User.objects.filter(email = attrs.get('email', '')).exists()):
            raise serializers.ValidationError({"Email" : "Alreafy Exists"})
        if(User.objects.filter(username = attrs.get("username")).exists()):
            raise serializers.ValidationError({"Username" : "ALrady EXists"})
        return super().validate(attrs)
    
    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)