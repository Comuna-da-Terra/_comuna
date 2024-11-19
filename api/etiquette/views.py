from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import render

from permissions import IsSuperuser
from accounts.models import User



class EtiquetteView(APIView):
    permission_classes =        [IsAuthenticated, IsSuperuser]
    authentication_classes =    [JWTAuthentication]

    def post(self, request):
        pedidos = request.data
        etiquetas = []
        for pedido in pedidos:
            client = User.objects.filter(id = pedido['id_client']).first()
            telefone = client.cellphone 
            quantidade_total = 0
            itens_etiqueta = []
            subtotal = 0

            for produto in pedido['order_product']:
                quantidade_total += produto['quantity']
                subtotal +=         produto['total_price']
                itens_etiqueta.append({
                    'quantidade':   produto['quantity'],
                    'preco':        produto['total_price'],
                    'nome':         produto['name'],
                })

            etiquetas.append({
            'quantidade_total':     quantidade_total,
            'delivery':             pedido['delivery'],
            'endereco':             pedido['address'],
            'cliente':              pedido['client'],
            'itens':                itens_etiqueta,
            'telefone':             telefone,
            'subtotal':             subtotal,
        })

        context = {'etiquetas': etiquetas}
        return render(request, 'etiquette.html', context)