from django.db.models.signals import pre_save, pre_delete
from rest_framework.exceptions import ValidationError
from django.dispatch import receiver

from orders.models import ProductOrder

@receiver(pre_save, sender=ProductOrder)
def update_stock_pre_save(sender, instance, **kwargs):
    order_product = ProductOrder.objects.filter(pk=instance.pk)
    product = instance.product
    already_product = ProductOrder.objects.filter(product=instance.product)

    if not order_product.exists():
        product.likely_stock -= int(instance.quantity)
        product.save()
    else:

        original_order = ProductOrder.objects.get(pk=instance.pk)
        product.likely_stock += original_order.quantity
        print(product.likely_stock)
        print(int(instance.quantity))
        if product.likely_stock < int(instance.quantity):
            raise ValidationError({"detail": ["Não temos essa quantidade solicitada, para o produto " + product.name]}) 
        product.likely_stock -= int(instance.quantity)
        product.save()

@receiver(pre_delete, sender=ProductOrder)
def update_stock_pre_delete(sender, instance, **kwargs):
    product = instance.product
    
    product.likely_stock += int(instance.quantity)
    product.save()