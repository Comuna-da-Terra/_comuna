from django.db import models
from accounts.models import User
import uuid

class Wallet(models.Model):
    id                          = models.UUIDField(
        default         = uuid.uuid4,
        primary_key     = True,
        editable        = False
    )

    user                        = models.ForeignKey(User,on_delete=models.CASCADE,related_name='wallets')
    valuation                   = models.DecimalField(max_digits=6, decimal_places=2, default= 0, )

    created_at                  = models.DateTimeField(auto_now_add=True)
    updated_at                  = models.DateTimeField(auto_now=True)

    