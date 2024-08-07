from adresses.models import Address
from products.models import Product
from accounts.models import User
from django.db import models
import uuid

class Order(models.Model):
    id                          = models.UUIDField(
        default         = uuid.uuid4,
        primary_key     = True,
        editable        = False,
    )

    user                        = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_address            = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)

    STATUS_CHOICES              = [
        (1, ("In process")),
        (2, ("Completed")),
        (3, ("Finished")),
        (4, ("Delivered")),
        ]
    status                      = models.IntegerField(choices=STATUS_CHOICES, default=1)
    subtotal                    = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    delivery_home               = models.BooleanField(default=False)
    

    active                      = models.BooleanField(default=True)
    created_at                  = models.DateTimeField(auto_now_add=True)
    updated_at                  = models.DateTimeField(auto_now=True)

    # def __str__(self) -> str:
    #     return str(self.id)
    class Meta:
        verbose_name            = "Pedido"

class ProductOrder(models.Model):
    id                          = models.UUIDField(
        default         = uuid.uuid4,
        primary_key     = True,
        editable        = False,
    )

    user                        = models.ForeignKey(User, on_delete=models.CASCADE)
    order                       = models.ForeignKey(Order, on_delete=models.CASCADE)
    product                     = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    quantity                    = models.PositiveIntegerField(default=1)
    total_price                 = models.DecimalField(max_digits=10, decimal_places=2)

    created_at                  = models.DateTimeField(auto_now_add=True)
    updated_at                  = models.DateTimeField(auto_now=True)

    # def __str__(self) -> str:
    #     return str(self.id, self.quantity, self.total_price)
    class Meta:
        verbose_name            = "Produto Pedido"
