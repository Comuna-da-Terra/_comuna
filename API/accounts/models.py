from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.utils import timezone

class User(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    email = models.EmailField(max_length=256, unique=True)
    username = models.CharField(max_length=150, unique=False, blank=True)
    password = models.CharField(max_length=256)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # cpf = models.CharField(max_length=14)
    birth_date = models.DateField(default=timezone.now)
    cellphone = models.CharField(max_length=11, null=False)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name + " > > " + self.email


# class Cliet(User):
# IMPROVE

# class Producer(User):
# IMPROVE
