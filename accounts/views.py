from .models import User

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView, Response, Request, status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .serializer import CustomJWTSerializer
from .serializer import UserSerializer
from .permissions import IsAccountOwnerOrSuperuser, IsSuperuser

from django.shortcuts import get_object_or_404
import pdb

class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]
    queryset = User.objects.all()

    serializer_class = UserSerializer


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = UserSerializer
    queryset = User

    def get(self, request: Request) -> Response:
        user = get_object_or_404(User, id=request._auth.payload['user_id'])
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def patch(self, request: Request) -> Response:
        user = get_object_or_404(User, id=request._auth.payload['user_id'])
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)

    def delete(self, request: Request) -> Response:
        user = get_object_or_404(User, id=request._auth.payload['user_id'])
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer
