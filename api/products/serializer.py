from .models import Product, Category

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from orders.serializer import OrderSerializer, ProductOrderSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "stock",
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