from .models import Order, ProductOrder

from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from django.shortcuts import get_object_or_404

from .permissions import IsAccountOwnerOrSuperuser, IsSuperuser
from .serializer import ProductOrderSerializer, OrderSerializer

class ProductOrderView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrSuperuser]
    
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return ProductOrder.objects.all()
        
        order = Order.objects.filter(active = True)
 
        return ProductOrder.objects.filter(id_order=order[0].id)

    def perform_create(self, serializer):

        serializer.save(
            user    = self.request.data.get('user'),
            id_product = self.request.data.get('id_product'),
            quantity = self.request.data.get('quantity'),
            # user = self.request.data.user
            # type = self.request.data.get('type')
        )   


class ProductOrderDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrSuperuser]

    def delete(self, request, pk, format=None):
        product_order = get_object_or_404(ProductOrder, id=pk)
        serializer = ProductOrderSerializer()
        serializer.delete(product_order)

        return Response({'message': 'ProductOrder excluído com sucesso.'}, status=status.HTTP_200_OK)
    
class OrderPartialUpdateView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrSuperuser]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrSuperuser]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.all()
        
        return Order.objects.filter(user_id=self.request.user.id)

class OrderDeleteView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrSuperuser]

    def delete(self, request, pk, format=None):
        order = get_object_or_404(Order, id=pk)
        serializer = OrderSerializer()
        serializer.delete(order)

        return Response({'message': 'Ordem, deletada!.'}, status=status.HTTP_200_OK)