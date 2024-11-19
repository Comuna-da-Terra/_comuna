from rest_framework import serializers
from .models import BasketPlan, BasketDelivered

class BasketPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketPlan
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]

    
    # def create(self, validated_data):
    #     return super().create(validated_data)

    def update(self, instance: BasketPlan, validated_data: dict) -> BasketPlan:

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    
class BasketDeliveredSerialzier(serializers.ModelSerializer):
    class Meta:
        model = BasketDelivered
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]

                