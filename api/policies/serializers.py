from .models import Policy, UserPolicy
from rest_framework import serializers

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = [
            "id",
            "type",
            "content",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
      
        current_policy = Policy.objects.filter(type=validated_data["type"]).first()

        if current_policy:

            current_policy.content = validated_data["content"]
            current_policy.save()
            return current_policy
        else:

            return Policy.objects.create(**validated_data)

