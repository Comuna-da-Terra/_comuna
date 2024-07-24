from django.db import models
import uuid
from accounts.models import User

class Payment(models.Model):
    id                          = models.UUIDField(
        default         = uuid.uuid4,
        primary_key     = True,
        editable        = False,
    )

    date_payment = models.DateField()
    value_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payment")

    created_at                  = models.DateTimeField(auto_now_add=True)
    updated_at                  = models.DateTimeField(auto_now=True)
