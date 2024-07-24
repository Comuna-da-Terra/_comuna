from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Wallet
from .permissions import IsAccountOwnerOrSuperuser, IsSuperuser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import WalletSerializer
from  django.shortcuts import get_object_or_404


from rest_framework.views import APIView

class WalletViews(APIView):
    authentication_classes      = [JWTAuthentication]
    permission_classes          = [IsAuthenticated, IsAccountOwnerOrSuperuser]
    serializer_class            = WalletSerializer

    def get(self, request):
        wallet, created         = Wallet.objects.get_or_create(user = self.request.user)
        serializer              = WalletSerializer(wallet)

        return Response(serializer.data, status=status.HTTP_200_OK)
 
    def patch(self, request, pk):
        wallet                  = self.get_object_or_404(pk)
        serializer              = WalletSerializer(wallet, request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class AllWalletsView(APIView):
    authentication_classes      = [JWTAuthentication]
    permission_classes          = [IsAuthenticated, IsSuperuser]
    serializer_class            = WalletSerializer

    def get(self, request):
        wallets                 = Wallet.objects.all()
        serializer              = WalletSerializer(wallets, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)