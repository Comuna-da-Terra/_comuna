from django.db import models
from accounts.models import User
from products.models import Product
import uuid

class Order(models.Model):
    id= models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    delivery = models.BooleanField(default=False)

    active = models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    # def __str__(self) -> str:
    #     return str(self.id)
    class Meta:
        verbose_name = "Pedido"

class ProductOrder(models.Model):
    id= models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    id_order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="id_order")
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="id_product")
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    # def __str__(self) -> str:
    #     return str(self.id, self.quantity, self.total_price)
    class Meta:
        verbose_name = "Produto Pedido"

