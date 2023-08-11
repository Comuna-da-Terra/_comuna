from .models import Product, Category

from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

class ProductSerializer(ModelSerializer):
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
        read_only_fields = ["created_at", "updated_at"]
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
