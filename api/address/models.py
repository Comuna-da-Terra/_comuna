from django.db import models
import uuid

class Address(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    country = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    neighborhood = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    reference = models.CharField(max_length=256)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.city + " " + self.state + " > > " + self.country

