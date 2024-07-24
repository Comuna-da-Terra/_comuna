from django.core.management.base import BaseCommand

from products.models import Product, Category
from products.models import Product
from random import randint, choice
from decimal import Decimal
import uuid

class Command(BaseCommand):
    help = 'Create multiples products'

    def handle(self, *args, **kwargs):
        category, created = Category.objects.get_or_create(name='Categoria Padrão')
        for i in range(30):
            product = Product(
                id=uuid.uuid4(),
                name=f'Produto {i}',
                likely_stock=randint(1, 20),
                garanteed_stock=randint(1, 20),
                stock=randint(1, 20),
                price=Decimal(randint(1, 100)),
                type=choice(['Comum', 'P', 'M', 'G']),
                category=category
            )
            product.save()
