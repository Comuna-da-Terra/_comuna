from .models import Product,Category
from orders.models import ProductOrder, Order

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status

from permissions import IsAccountOwnerOrSuperuser, IsSuperuser
from .serializers import ProductSerializer, ProductsInOrderAccountSerializer, CategorySerializer
from .pagination import PaginationProducts

from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import process_product_file
from django.core.exceptions import ValidationError


class ProductView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsSuperuser]
    pagination_class = PaginationProducts
        
    queryset = Product.objects.filter(likely_stock__gt=0).order_by('name')
        

    serializer_class = ProductSerializer

class ProductsListView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsSuperuser]
        
    queryset = Product.objects.filter(likely_stock__gt=0).order_by('name')
        
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
        user_orders = Order.objects.filter(user=user).exclude(status=4)
        if not user_orders.exists():
            return Response({'detail': 'Nenhum pedido encontrado para este usuário.'}, status=status.HTTP_404_NOT_FOUND)

        response['order'] = user_orders[0]
        response['order_products'] = ProductOrder.objects.filter(order=user_orders[0].id)
        response['products'] = Product.objects.filter(id__in=[op.product.id for op in response['order_products']])

        data = {'order': response['order'], 'order_products': response['order_products'], 'products': response['products']}

        serializer = ProductsInOrderAccountSerializer(data)
        return Response(serializer.data)

class CategoryView(APIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsSuperuser]

    serializer_class = CategorySerializer

    def get(self, request):
        
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        self.permission_classes = [IsSuperuser]
        self.check_permissions(request)

        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UploadProdutosView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return Response({"error": "Nenhum arquivo enviado"}, status=status.HTTP_400_BAD_REQUEST)

        excel_file = request.FILES['file']
        
        try:
            process_product_file(excel_file)
            return Response({"message": "Produtos importados com sucesso!"}, status=status.HTTP_200_OK)
        
        except ValidationError as e:
            return Response({"error": f"Erro: {e}"}, status=status.HTTP_400_BAD_REQUEST)