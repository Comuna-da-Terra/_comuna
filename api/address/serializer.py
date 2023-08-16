from .models import Address

from rest_framework.serializers import ModelSerializer


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__" 
        read_only_fields = ["created_at", "updated_at"]
        
    
    