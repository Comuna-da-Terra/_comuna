from django.contrib import admin
from .models import Policy, UserPolicy

class PolicyAdmin(admin.ModelAdmin):
  

    admin.site.register(Policy)
    admin.site.register(UserPolicy)
