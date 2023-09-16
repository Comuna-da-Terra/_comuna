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
    first_name          = models.CharField(max_length=30)
    last_name           = models.CharField(max_length=30)
    # cpf               = models.CharField(max_length=14)
    birth_date          = models.DateField(default=timezone.now)
    cellphone           = models.CharField(max_length=11, null=False)
    is_active           = models.BooleanField(default=True)

    address             = models.OneToOneField(
        "adresses.Address",
        null            = True,
        on_delete       = models.SET_NULL,
        related_name    ='user'
    ) 
    
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    USERNAME_FIELD      = "email"
    REQUIRED_FIELDS     = ["username"]

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name + " > > " + self.email


class Client(User):

    level               = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name    = "Cliente"
    


class Member(User):
    coop_number         = models.PositiveIntegerField(unique=True )

    class Meta:
        verbose_name    = "Cooperado"