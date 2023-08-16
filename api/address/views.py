from .models import Address

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .permissions import IsAccountOwnerOrSuperuser, IsSuperuser
from .serializer import AddressSerializer

class AddressView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]
    
    queryset = Address.objects.all()
        
    serializer_class = AddressSerializer
