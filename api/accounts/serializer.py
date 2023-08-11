from .models import User, Client, Member

from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth.hashers import make_password
from .utils.random_username import random_username
from hashlib import sha256
import ipdb



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__" 
        # [
        #     "id",
        #     "first_name",
        #     "last_name",
        #     "birth_date",
        #     "username",
        #     "email",
        #     "password",
        #     "cellphone",
        #     "created_at",
        #     "updated_at",
        # ]
        read_only_fields = ["created_at", "updated_at"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "validators": [UniqueValidator(queryset=User.objects.all())],
            },
        }

    def create(self, validated_data) -> Client or Member:
        
        member = 'coop_number' in validated_data
    
        if member:
            member = Member.objects.create(**validated_data)

            return member
        else:
            client = Client.objects.create(**validated_data)
            return client


        # total_price = product.price * validated_data['quantity']
        # order.subtotal = order.subtotal + total_price

        # order.save()

        # product_order = ProductOrder.objects.create(
        #     id_order=order,
        #     id_product=product,
        #     quantity=validated_data['quantity'],
        #     total_price=total_price
        # )

        # return product_order
             

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

        return token
