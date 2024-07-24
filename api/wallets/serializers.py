from rest_framework import serializers
from .models import Wallet

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ["id", "valuation", "user",]
        read_only_fields = ["created_at", "updated_at"]

        def update(self, instance: Wallet, validated_data: dict) -> Wallet:

            for key, value in validated_data.items():
                setattr(instance, key, value)
            instance.save()
            return instance