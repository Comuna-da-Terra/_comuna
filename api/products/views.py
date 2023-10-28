from .models import Product,Category
from orders.models import ProductOrder, Order

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status

from .permissions import IsAccountOwnerOrSuperuser, IsSuperuser
from .serializer import ProductSerializer, ProductsInOrderAccountSerializer, CategorySerializer

from rest_framework.response import Response
from rest_framework.views import APIView

class ProductView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]
    
    queryset = Product.objects.all()
        
    serializer_class = ProductSerializer

    
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrSuperuser]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductsInOrderAccountView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrSuperuser]

    serializer_class = ProductSerializer

    def get(self, request):
        user = self.request.user.id
        response = {}

        user_orders = Order.objects.filter(user=user).exclude(status=3)
        if not user_orders.exists():
            return Response({'detail': 'Nenhum pedido encontrado para este usuário.'}, status=status.HTTP_404_NOT_FOUND)

        response['order'] = user_orders[0]
        response['order_products'] = ProductOrder.objects.filter(id_order=user_orders[0].id)
        response['products'] = Product.objects.filter(id__in=[op.id_product.id for op in response['order_products']])

        data = {'order': response['order'], 'order_products': response['order_products'], 'products': response['products']}

        serializer = ProductsInOrderAccountSerializer(data)
        return Response(serializer.data)

class CategoryView(APIView):
    
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        print(categories)

        return Response(serializer.data)
