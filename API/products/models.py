from django.db import models
import uuid

class Category(models.Model):
    id= models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    name= models.CharField(max_length=30, unique=True)
    description= models.CharField(max_length=100)

    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Categoria"

class Product(models.Model):
    id= models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    name= models.CharField(max_length=30, unique=True)
    stock= models.IntegerField(default=1)
    price= models.IntegerField()
    TYPE_CHOICES = [
        ("D", ("Padrão")),
        ("P", ("Pequeno")),
        ("M", ("Médio")),
        ("G", ("Grande")),]
    type= models.CharField(max_length=1, choices=TYPE_CHOICES, default="D")

    category= models.ForeignKey(
        "products.Category",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="product_category")

    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name + " " + self.type
    class Meta:
        verbose_name = "Produto"