
from .models import Order, ProductOrder
from rest_framework import serializers

from products.models import Product
from accounts.models import User

from django.shortcuts import get_object_or_404
from django.db.models import Sum
# import ipdb

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Order
        fields  = "__all__"

class ProductOrderSerializer(serializers.ModelSerializer):
    id_order    = OrderSerializer(read_only=True)
    id_product  = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model   = ProductOrder
        fields  = "__all__"
        read_only_fields = [
            "total_price",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        account                                 = get_object_or_404(User, pk=validated_data['id_user'])
        product                                 = get_object_or_404(Product, pk=validated_data['id_product'])

        order, created                          = Order.objects.get_or_create(owner=account, active=True,)
        verify_product_order                    = ProductOrder.objects.filter(id_order=order, id_product=product).first()

        if verify_product_order:
            verify_product_order.quantity       = verify_product_order.quantity + validated_data['quantity']
            verify_product_order.total_price    = product.price * verify_product_order.quantity
            verify_product_order.save()

            order.subtotal  = ProductOrder.objects.filter(id_order=order).aggregate(Sum('total_price'))['total_price__sum']
            order.save()

            return verify_product_order

        total_price                             = product.price * validated_data['quantity']
        order.subtotal                          = order.subtotal + total_price

        order.save()

        product_order                           = ProductOrder.objects.create(
            id_order=order,
            id_product=product,
            quantity=validated_data['quantity'],
            total_price=total_price
        )

        return product_order

    def delete(self, instance):
        order                                   = instance.id_order
        # product                                 = instance.id_product
        order.subtotal                         -= instance.total_price
        order.save()

        instance.delete()
