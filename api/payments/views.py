from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from permissions import IsSuperuser
from rest_framework import status
from rest_framework.response import Response
from .serializers import PaymentSerializer

class PaymentView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
