from .models import User

from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "write_only": True,
                "validators": [UniqueValidator(queryset=User.objects.all())],
            },
        }

    def create_user(self, email, username, password, alias=None):
        user = self.model(
            email = self.normalize_email(email),
            username = username,)
        user.set_password(password)
        user.save()

        return user
            
    def validate_password(self, value: str) -> str:
        return make_password(value)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()

        return instance

class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod                                
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser

        return token
