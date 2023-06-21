from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    email = models.EmailField( max_length=256, unique=True )
    password = models.CharField( max_length=256 )
    first_name = models.CharField( max_length=20 )
    last_name = models.CharField( max_length=30 )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField( auto_now_add=True )
    updated_at = models.DateTimeField( auto_now=True )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username + " >> " + self.email