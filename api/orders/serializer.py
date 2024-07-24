from .models import Order, ProductOrder
from products.models import Product
from accounts.models import User

from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.db.models import Sum
from decimal import Decimal
# import ipdb


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model                                   = Order
        fields                                  = "__all__"

    # def update(self, instance, validated_data):
    #     status                                  = self.context['request'].data.get('status')
    #     orders_products                         = ProductOrder.objects.filter(order=instance.id)

    #     if status == 2:
    #         for order in orders_products:
    #             product                         = order.product
    #             quantity                        = order.quantity
    #             if product.likely_stock >= quantity:
    #                 product.likely_stock        -= quantity
    #                 product.save()
    #             elif product.likely_stock < order.quantity:
    #                 raise serializers.ValidationError({"detail": ["Não temos essa quantidade solicitada, para o produto " + product.name]})
    #     elif status == 1:
    #         for order in orders_products:
    #             product                         = order.product
    #             quantity                        = order.quantity
    #             product.likely_stock            += quantity
    #             product.save()

    #     instance = super().update(instance, validated_data)
    #     return instance


    def delete(self, instance):
        order                                   = instance
        orders_products                         = ProductOrder.objects.filter(order = order.id)
        for op in orders_products:
            op.delete()

        instance.delete()



class ProductOrderSerializer(serializers.ModelSerializer):
    order                                       = OrderSerializer(read_only=True)
    product                                     = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        model                                   = ProductOrder
        fields                                  = "__all__"
        read_only_fields                        = ["total_price", "created_at", "updated_at",]
        extra_kwargs                            = {'total_price': {'read_only': True},
        }

    def create(self, validated_data):
        account                                 = get_object_or_404(User, pk=validated_data['user'])
        product                                 = get_object_or_404(Product, pk=validated_data['product'])
        quantity                                = int(validated_data['quantity'])

        order, created                          = Order.objects.get_or_create(user=account,**{'status__lte': 3} )
        verify_product_order                    = ProductOrder.objects.filter(order=order, product=product).first()

        if verify_product_order:
            verify_product_order.quantity       = validated_data['quantity']
            verify_product_order.total_price    = product.price * int(verify_product_order.quantity)
            verify_product_order.save()

            order.subtotal                      = ProductOrder.objects.filter(order=order).aggregate(Sum('total_price'))['total_price__sum']
            order.save()
            return verify_product_order
        
        total_price                             = product.price * Decimal(validated_data['quantity'])
        order.subtotal                          = order.subtotal + total_price
        order.save()
        product_order                           = ProductOrder.objects.create(
            order                               = order,
            product                             = product,
            user                                = account,
            quantity                            = validated_data['quantity'],
            total_price                         = total_price
            
        )
        return product_order
    
    # def update(self, instance, validated_data):
    #     quantity                                = validated_data["quantity"]
    #     product                                 = instance.product
        
    #     if quantity == 0: 
    #         instance.delete()
    #     instance.quantity                       = int(validated_data.get('quantity', instance.quantity))
    #     instance.total_price                    = Decimal(instance.product.price * instance.quantity)
    #     instance.save()

    #     order                                   = instance.order
    #     order.subtotal                          = ProductOrder.objects.filter(order=order).aggregate(Sum('total_price'))['total_price__sum']
    #     order.save()

    #     return instance

    def delete(self, instance):
        order                                   = instance.order
        order.subtotal                          -= instance.total_price
        order.save()

        instance.delete()
        order_products                          = ProductOrder.objects.filter(order = order.id)
        
        if order_products.exists() == False:
            order.delete()
