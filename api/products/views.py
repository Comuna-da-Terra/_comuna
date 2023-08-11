from .models import Product,Category

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .permissions import IsAccountOwnerOrSuperuser, IsSuperuser
from .serializer import ProductSerializer

class ProductView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]
    
    queryset = Product.objects.all()
        
    serializer_class = ProductSerializer

    
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]

    queryset = Product.objects.all()

    serializer_class = ProductSerializer
