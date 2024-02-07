from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models
import uuid

class User(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    email               = models.EmailField(max_length=256, unique=True)
    username            = models.CharField(max_length=150, unique=False, blank=True)
    password            = models.CharField(max_length=256)
    name                = models.CharField(max_length=100)
    cpf                 = models.CharField(max_length=11, unique=False)
    birth_date          = models.DateField(default=timezone.now)
    cellphone           = models.CharField(max_length=15, null=False)
    is_active           = models.BooleanField(default=True)

    coop_number         = models.PositiveIntegerField(unique=True, null=True, blank=True )
    # level               = models.PositiveIntegerField(default=0)         
    
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    USERNAME_FIELD      = "email"
    REQUIRED_FIELDS     = ["username"]

    def __str__(self) -> str:
        return self.name + " " " > > " + self.email