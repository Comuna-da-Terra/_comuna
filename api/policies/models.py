from django.db import models

from django.db import models
import uuid

from accounts.models import User

class Policy(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    TYPE_CHOICES = [
        ("termos", ("Termos de Uso")),
        ("privacidade", ("Politica de Privacidade")),]
    type= models.CharField( choices=TYPE_CHOICES, max_length=13, null=False, blank=False)

    content = models.TextField(null=False, blank=False)

    # is_active           = models.BooleanField(default=True)

    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)


class UserPolicy(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    
    user                        = models.ForeignKey(User, on_delete=models.CASCADE)
    policy                       = models.ForeignKey(Policy, on_delete=models.PROTECT)
    approval = models.BooleanField(default=False)
    
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User: {self.user}, Policy: {self.policy}, Approved: {self.approval}"

