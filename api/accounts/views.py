from .models import User

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .permissions import IsAccountOwnerOrSuperuser, IsSuperuser
from .serializer import CustomJWTSerializer
from .serializer import UserSerializer
from accounts.utils.random_username import random_username

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
        
    def perform_create(self, serializer):
        serializer.save(
            username=random_username(),
        )

class ListUserView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrSuperuser]
    serializer_class = UserSerializer
        
    def get_queryset(self):
            return User.objects.filter(id=self.request.user.id)
    
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwnerOrSuperuser]

    queryset = User.objects.all()

    serializer_class = UserSerializer



# _________________________________________AUTH_VIEW
class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer

class TokenVerifyView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'valid': True}, status=status.HTTP_200_OK)