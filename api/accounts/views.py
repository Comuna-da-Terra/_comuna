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
from .serializer import UserSerializer, PasswordChangeSerializer
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


class PasswordChangeAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwnerOrSuperuser]
    serializer_class = PasswordChangeSerializer 
    
    def patch(self, request, format=None):
        serializer = PasswordChangeSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            current_password = serializer.validated_data['current_password']
            new_password = serializer.validated_data['new_password']
            confirm_password = serializer.validated_data['confirm_password']

            if not request.user.check_password(current_password):
                return Response({'error': 'Senha atual incorreta.'}, status=status.HTTP_400_BAD_REQUEST)

            if new_password != confirm_password:
                return Response({'error': 'As senhas não estão semelhantes.'}, status=status.HTTP_400_BAD_REQUEST)

            user = request.user
            user.set_password(new_password)
            user.save()

            return Response({'success': 'Senha alterada com sucesso.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

# _________________________________________AUTH_VIEW
class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer

class TokenVerifyView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'valid': True}, status=status.HTTP_200_OK)