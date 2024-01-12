from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import User

from django.contrib.auth.hashers import make_password
from .utils.random_username import random_username
from hashlib import sha256
import ipdb



class UserSerializer(ModelSerializer):
    class Meta:
        model               = User
        fields              = [
            "id",
            "birth_date",
            "name",
            "cellphone",
            "password",
            "email",
            "coop_number",
            "is_superuser",
            "is_staff"
            ] 
        read_only_fields    = ["created_at", "updated_at"]
        extra_kwargs        = {
            "password": {"write_only": True},
            "email": {
                "validators": [UniqueValidator(queryset=User.objects.all())],
            },
        }

    def create(self, validated_data) -> User:
        member              = 'coop_number' in validated_data
    
        if member:
            member          = User.objects.create(**validated_data)
            return member
        else:
            client          = User.objects.create(**validated_data)
            return client
             

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
                setattr(instance, key, value)
        instance.save()
        return instance
    
    def validate_password(self, value: str) -> str:
        return make_password(value)


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser
        user.save(update_fields=["last_login"])
        
        return token

class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)


