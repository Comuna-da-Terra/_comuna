from django.contrib import admin
from .models import Order, ProductOrder

class ProdOrderAdmin(admin.ModelAdmin):
    fields = [
        "id_product",
        "quantity"
    ]

admin.site.register(Order)
admin.site.register(ProductOrder, ProdOrderAdmin)

# Register your models here.
