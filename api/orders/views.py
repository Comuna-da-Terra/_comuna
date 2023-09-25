from .models import Order, ProductOrder

from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.shortcuts import get_object_or_404

from .permissions import IsAccountOwnerOrSuperuser, IsSuperuser
from .serializer import ProductOrderSerializer

class ProductOrderView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAccountOwnerOrSuperuser]
    
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer

    # def get(self, request, *args, **kwargs):
    #     order = Order.objects.filter(active=True, user=request.user)
    #     product_orders = ProductOrder.objects.filter(id_order=order.id)
    #     serializer = ProductOrderSerializer(product_orders, many=True)

    #     return Response(serializer.data)

    def perform_create(self, serializer):

        serializer.save(
            id_user    = self.request.user.id,
            id_product = self.request.data.get('id_product'),
            quantity = self.request.data.get('quantity')
        )    

class ProductOrderDeleteView(APIView):
    authentication_classes = [JWTAuthentication]

    def delete(self, request, format=None):
        product_order_id = request.data.get('id')
        product_order = get_object_or_404(ProductOrder, id=product_order_id)

        serializer = ProductOrderSerializer()
        serializer.delete(product_order)

        return Response({'message': 'ProductOrder excluído com sucesso.'}, status=status.HTTP_200_OK)