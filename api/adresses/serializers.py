from rest_framework import serializers
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    number                  = serializers.CharField(
        error_messages      = {"required": "O campo 'number' é obrigatório e não pode estar vazio."},
    )

    class Meta:
        model               = Address
        fields              = "__all__"
        read_only_fields    = [
            "created_at",
            "updated_at",  
        ]
        extra_kwargs        = {
            "complement":   {"allow_null": True},
            "number":       {"allow_null": True},
            "state":        {"allow_null": True},
            "uf":           {"allow_null": True},
        }
        
    def update_address(self, instance: Address, validated_data: dict) -> Address:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance