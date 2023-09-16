from django.contrib import admin
from .models import User, Client, Member
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(admin.ModelAdmin):
    pass

class ClientAdmin(admin.ModelAdmin):
    fields = [
        "email",
        "username",
        "password",
        "first_name",
        "last_name",
        # "cpf",
        "birth_date",
        "cellphone"
        ]


admin.site.register(User, CustomUserAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Member)
