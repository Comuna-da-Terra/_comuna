from rest_framework import serializers
from .models import Payment
from wallets.models import Wallet

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "user",
            "date_payment",
            "value_payment",
        ]
        read_only_fields = ["created_at", "updated_at",]

    def create(self, validated_data):
        wallet = Wallet.objects.get(user=validated_data['user'])

   
        wallet.valuation -= validated_data['value_payment']
        wallet.save()
 
        return super().create(validated_data)