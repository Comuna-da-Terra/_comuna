from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(admin.ModelAdmin):
    pass

class ClientAdmin(admin.ModelAdmin):
    fields = [
        "email",
        "username",
        "password",
        "name",
        # "cpf",
        "birth_date",
        "cellphone",
        "coop_number"
        ]


admin.site.register(User, CustomUserAdmin)
# admin.site.register(Client, ClientAdmin)
# admin.site.register(Member)
