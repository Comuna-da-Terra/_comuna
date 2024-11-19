from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from  django.shortcuts import get_object_or_404

from permissions import IsAccountOwnerOrSuperuser, IsSuperuser
from utils.basketPlans_util import create_basket_deliveries
from .serializers import BasketPlanSerializer
from .models import BasketPlan

class BasketPlanView(generics.ListCreateAPIView):
    authentication_classes          = [JWTAuthentication]
    permission_classes              = [IsAuthenticated, IsAccountOwnerOrSuperuser]
    serializer_class                = BasketPlanSerializer

    def post(self, request):
        request.data['user']        = request.user.id
        request.data['is_active']   = True
        serializer                  = BasketPlanSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        plan = BasketPlan.objects.filter(user=request.user).first()
        serializer = BasketPlanSerializer(plan)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ListAllBasketPlansView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]
    serializer_class = BasketPlanSerializer

    def get_queryset(self):
        if(self.request.user.is_superuser):
            return BasketPlan.objects.all()

class EditBasketPlanView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwnerOrSuperuser]
    serializer_class = BasketPlanSerializer

    def patch(self, request):
        print(request.data["id"])
        basketPlan              = get_object_or_404(BasketPlan, pk=request.data["id"])
        serializer              = BasketPlanSerializer(basketPlan, request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CreateDeliveriesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperuser]

    def post(self, request):
        result = create_basket_deliveries()
        
        if result["created"]:
            return Response(
                {
                    "message": "Entregas criadas com sucesso.",
                    "created": result["created"],
                    "already_exists": result["already_exists"]
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    "message": "Nenhuma nova entrega criada. Todas as entregas já existiam.",
                    "already_exists": result["already_exists"]
                },
                status=status.HTTP_200_OK
            )
            
        