from rest_framework.response import Response
from rest_framework import generics, status

from .serializers import PolicySerializer
from .models import Policy

class PolicyView(generics.ListCreateAPIView):
    serializer_class        = PolicySerializer

    def post(self, request):
        serializer = PolicySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        policy_type = request.query_params.get('type')

        if not policy_type:
            return Response({'error': 'O parâmetro "type" é necessário.'}, status=status.HTTP_400_BAD_REQUEST)

        policy = Policy.objects.filter(type=policy_type).first()
        if policy:
            serializer = PolicySerializer(policy)
            return Response(serializer.data)
        else:
            return Response({'error': f'Política de tipo "{policy_type}" não encontrada.'}, status=status.HTTP_404_NOT_FOUND)
