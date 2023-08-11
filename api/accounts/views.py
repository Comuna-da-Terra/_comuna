from .models import User

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .permissions import IsAccountOwnerOrSuperuser, IsSuperuser
from .serializer import CustomJWTSerializer
from .serializer import UserSerializer
from accounts.utils.random_username import random_username

class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrSuperuser]

    serializer_class = UserSerializer
    
    def get_queryset(self):
        if(self.request.user.is_superuser): 
            return User.objects.all()
        else:
            return User.objects.filter(id=self.request.user.id)
        
    serializer_class = UserSerializer
    def perform_create(self, serializer):
        serializer.save(
            username=random_username(),
        )
    
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwnerOrSuperuser]

    queryset = User.objects.all()

    serializer_class = UserSerializer

class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer

# class UserDetailView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     serializer_class = UserSerializer
#     queryset = User

#     # def post(self, request: Request) -> Response:
#     #     serializer = UserSerializer(request)

#     def get(self, request: Request) -> Response:
#         user = get_object_or_404(User, id=self.request.user.id)
#         serializer = UserSerializer(user)

#         return Response(serializer.data)

#     def patch(self, request: Request) -> Response:
#         user_id = self.request.user.id
#         user = get_object_or_404(User, id=user_id)
#         serializer = UserSerializer(user, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)

#         serializer.save()

#         return Response(serializer.data)

#     def delete(self, request: Request) -> Response:
#         user = get_object_or_404(User, id=self.request.user.id)
#         user.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)