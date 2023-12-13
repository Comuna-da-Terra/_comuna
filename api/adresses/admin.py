from django.contrib import admin
from .models import Address


class AddressAdmin(admin.ModelAdmin):
    fields = [
    "neighborhood",
    "street",
    "city",
    "zip_code",
    "uf",
    "complement",
    "country",
    "number",  
    "state",    
    "is_default",
    "user"
]


admin.site.register(Address)
