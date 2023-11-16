from .models import Order, ProductOrder
from accounts.models import User
from adresses.models import Address

from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from django.shortcuts import get_object_or_404

import pandas as pd
from django.http import HttpResponse, JsonResponse

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
 
        return ProductOrder.objects.filter(order=order[0].id)

    def perform_create(self, serializer):

        serializer.save(
            user    = self.request.data.get('user'),
            product = self.request.data.get('product'),
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
    
class ProductOrderUpdateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrSuperuser]

    def patch(self, request, pk, format=None):
        product_order = get_object_or_404(ProductOrder, id=pk)
        serializer = ProductOrderSerializer(instance=product_order, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save(instance=product_order)
            return Response({'message': 'Quantidade do produto atualizada com sucesso.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
    
class DetailsOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]

    def get(self, request):
        active_orders = Order.objects.filter(status=2).values()

        if active_orders.exists():
            data = []
            for index, order in enumerate(active_orders):
                client_user = User.objects.get( id = order["user_id"])
                address = Address.objects.get(id = order["delivery_address_id"])
                orderProducts = ProductOrder.objects.filter(order = order["id"])

                order_data = {
                    "client": client_user.name,
                    "delivery": order["delivery_home"],
                    "address": f"{address.street}, {address.number} - {address.neighborhood}",
                }
                order_data["order_product"] = []
                for orderProd in orderProducts:
                    order_data["order_product"].append({
                        "id": orderProd.id,
                        "id_product": orderProd.product.id,
                        "name": orderProd.product.name,
                        "quantity": orderProd.quantity
                    }
                    )
                data.append(order_data)

            return Response(data)
        else:
            return Response({'message': 'Sem Pedidos em aberto!'}, status=status.HTTP_404_NOT_FOUND)

class ExportCSVOrders(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrSuperuser]

    def get(self, request):
        active_orders = Order.objects.filter(status=2).values()
        df_to_export = []

        if active_orders.exists():
            for order in active_orders:
                client_user = User.objects.filter( id = order["user_id"])
                address = Address.objects.filter(id = order["delivery_address_id"])
                orderProducts = ProductOrder.objects.filter(order = order["id"])
                data = {
                    "DATA CRIAÇÃO": order["created_at"],
                    "DATA EDIÇÃO": order["updated_at"],
                    "ENTREGAR": order["delivery_home"],
                    "NOME COMPLETO": client_user[0].name,
                    "CELULAR": client_user[0].cellphone,
                    "ENDEREÇO": address[0].street + ", "+address[0].number + " - " + address[0].neighborhood,
                }
                for orderProd in orderProducts:
                    data[orderProd.product.name] = orderProd.quantity
            
                df_to_export.append(data)
        else:
            return Response({'message': 'Sem Pedidos em aberto!'}, status=status.HTTP_404_NOT_FOUND)
            

        df = pd.DataFrame(df_to_export)
        df.index = range(1, len(df) + 1)

        df['DATA CRIAÇÃO'] = pd.to_datetime(df['DATA CRIAÇÃO']).dt.strftime('%Y-%m-%d %H:%M:%S')
        df['DATA EDIÇÃO'] = pd.to_datetime(df['DATA EDIÇÃO']).dt.strftime('%Y-%m-%d %H:%M:%S')
        df['ENTREGAR'] = df['ENTREGAR'].replace({True: 'SIM', False: 'NAO'})

        excel_file_path = 'PEDIDOS.xlsx'


        df.to_excel(excel_file_path, engine='openpyxl')

        with open(excel_file_path, 'rb') as excel_file:
            content = excel_file.read()

        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = f'attachment; filename="{excel_file_path}"'
        response.write(content)

        return response
