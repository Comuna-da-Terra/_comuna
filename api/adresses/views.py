from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import Response, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Address
from .serializers import AddressSerializer
from accounts.models import User
from permissions import IsAccountOwnerOrSuperuser
import requests
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


class AddressView(ListCreateAPIView):
    authentication_classes  = [JWTAuthentication]
    permission_classes      = [IsAuthenticated, IsAccountOwnerOrSuperuser]
    serializer_class        = AddressSerializer

    def create(self, request, *args, **kwargs):
        if "zip_code" not in request.data or "country" not in request.data or "state" not in request.data:
            return Response(
                {"message": "Os campos de CEP, Pais, Estado e Número são obrigatórios!"},
                status.HTTP_400_BAD_REQUEST,
            )
        else:
            if len(request.data["zip_code"]) != 8:
                return Response(
                    {"message": "O campo 'zip_code' é obrigatório e deve conter 8 dígitos." },
                    status.HTTP_400_BAD_REQUEST
                )

            address_cep = request.data["zip_code"]
            cep = address_cep.replace("-", "").replace(".", "").replace(" ", "")
            try:
                req = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            except requests.ConnectionError:
                return Response(status.HTTP_400_BAD_REQUEST)

            dict_address = req.json()

            dict_address["city"]            = dict_address.get("localidade", "")
            dict_address["neighborhood"]    = dict_address.get("bairro", "")
            dict_address["uf"]              = dict_address.get("uf", "")
            dict_address["street"]          = dict_address.get("logradouro", "")
            request.data.update({**dict_address})

            request.data["user"] = request.user.id
            request.data["is_default"] = False

            return super().create(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Address.objects.all()
        
        return Address.objects.filter(Q(user_id=self.request.user) | Q(is_default=True))


class AddressDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes  = [JWTAuthentication]
    permission_classes      = [IsAuthenticated]
    serializer_class        = AddressSerializer

    queryset = Address.objects.all()


    def update(self, request, *args, **kwargs):
        address = self.get_object()

        if "zip_code" in request.data:
            if len(request.data["zip_code"]) != 8:
                return Response(
                    {"message": "O campo 'zip_code' é obrigatório e deve conter 8 dígitos." },
                    status.HTTP_400_BAD_REQUEST
                )
        
            address_cep                         = request.data["zip_code"]
            cep                                 = address_cep.replace("-", "").replace(".", "").replace(" ", "")

            try:
                req = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
                
                dict_address                    = req.json()
                dict_address["city"]            = dict_address.get("localidade", "")
                dict_address["neighborhood"]    = dict_address.get("bairro", "")
                dict_address["uf"]              = dict_address.get("uf", "")
                dict_address["street"]          = dict_address.get("logradouro", "")
                
                for key, value in dict_address.items():
                    setattr(address, key, value)
                address.save() 

            except requests.ConnectionError:
                return Response({"message": "Falha ao buscar dados de endereço"}, status.HTTP_400_BAD_REQUEST)
        request.data["is_default"] = False
        serializer  = self.get_serializer(address, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)