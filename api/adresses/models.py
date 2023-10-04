from django.db import models
from accounts.models import User
import uuid

class Address(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    neighborhood    = models.CharField(max_length=64, blank=True, null=True)
    street          = models.CharField(max_length=64, blank=True, null=True)
    city            = models.CharField(max_length=64, blank=True, null=True)
    zip_code        = models.CharField(max_length=8, blank=True, null=True)
    uf              = models.CharField(max_length=4, blank=True, null=True)
    complement      = models.TextField( blank=True, null=True)
    country         = models.CharField(max_length=64)
    number          = models.CharField(max_length=10)
    state           = models.CharField(max_length=64)
    is_default         = models.BooleanField(default=False)

    user = models.ForeignKey(
        "accounts.User",
        on_delete       = models.DO_NOTHING,
        related_name    ='addresses'
    ) 

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    # def __str__(self) -> str:
    #     return self.city + " " + self.state + " > > " + self.country