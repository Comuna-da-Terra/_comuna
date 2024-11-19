from django.shortcuts import render
from .models import User

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from permissions import IsAccountOwnerOrSuperuser, IsSuperuser
from .serializers import CustomJWTSerializer, UserSerializer, PasswordChangeSerializer, ResendTokenConfirm
from accounts.utils.random_username import random_username

from django.http import HttpResponse, JsonResponse
from .utils.generate_confirmation_token import generate_confirmation_token, confirm_token


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(
            username=random_username(),
        )

class ListUserView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwnerOrSuperuser]
    serializer_class = UserSerializer

    def get_queryset(self):
            return User.objects.filter(id=self.request.user.id)

class ListAllUserView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]
    serializer_class = UserSerializer

    def get_queryset(self):
        if(self.request.user.is_superuser):
            return User.objects.all()

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


# _________________________________________TOKEN_CONFIRM
def confirm_email(request, token):
    email = confirm_token(token)
    if email == "O token expirou.":
        link = '<a href="http://localhost:8000/api/reset_token_confirm/"> Novo link de ativação </a>'
        return HttpResponse(f'Token de confirmação inválido ou expirado.{link}')
    elif email == "Token inválido.":
        return HttpResponse("Token Invalido!")
    elif email:
        user = User.objects.get(email=email)
        user.is_active = True 
        user.save()
        return HttpResponse("E-mail confirmado com sucesso!")

def reset_token_confirm(request):
    return render(request, "token/reset-token-confirm.html", {"message": "O token de confirmação expirou. Por favor, solicite um novo."})

def resend_token_confirm(request):
    serializer = ResendTokenConfirm(data=request.POST)

    if serializer.is_valid():
        email = serializer.validated_data['email']
        return JsonResponse({"message": "Novo token gerado e enviado, por favor verifique seu e-mail!"}, status=200)
    
    return JsonResponse({"errors": serializer.errors}, status=400)