from django.shortcuts import get_object_or_404

from .models import Product, Category
from accounts.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from orders.serializers import OrderSerializer, ProductOrderSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            # IMG !!!
            "name",
            "likely_stock",
            "garanteed_stock",
            "price",
            "type",
            "category",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
                "name": {
                "validators": [UniqueValidator(queryset=Product.objects.all())],
            },
        }

    def create(self, validated_data):
        # account                                 = get_object_or_404(User, pk=validated_data['user'])
        category    = Category.objects.get_or_create(name= validated_data['category'])

        product = Product.objects.create(
            # # IMG !!!
            # name            = validated_data["name"],
            # likely_stock    = validated_data["likely_stock"],
            # garanteed_stock = validated_data["likely_stock"],
            # price           = validated_data["price"],
            # type            = validated_data["type"],
            # category        = category,
             **validated_data
        )
        return product
            

    def update(self, instance: Product, validated_data: dict) -> Product:

        for key, value in validated_data.items():
                setattr(instance, key, value)
        instance.save()
        return instance

class ProductsInOrderAccountSerializer(serializers.Serializer):
    order = OrderSerializer()
    order_products = ProductOrderSerializer(many=True)
    products = ProductSerializer(many=True)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
