from accounts.models import User
from django.db import models
import uuid

class BasketPlan(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )



    TYPE_PLAN_CHOICES = [("S", ("Semanal")),("Q", ("Quinzenal")),]
    type= models.CharField(max_length=5, choices=TYPE_PLAN_CHOICES, null=False, blank=False)
    
    TYPE_BASKET_CHOICES = [("M", ("Media")),("G", ("Grande")),]
    basket_type= models.CharField(max_length=5, choices=TYPE_BASKET_CHOICES, null=False, blank=False)

    user = models.ForeignKey(
        User,
        on_delete       = models.CASCADE,
        related_name    ='basket_plan'
    )
    is_active           = models.BooleanField(default=False) 

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    # def __str__(self) -> str:
    #     return self.city + " " + self.state + " > > " + self.country

class BasketDelivered(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )


    delivered           = models.BooleanField(default=False)
    delivered_date = models.DateTimeField()

    plan = models.ForeignKey(
        "basketplans.basketplan",
        on_delete       = models.CASCADE,
        related_name    ='basket_plan'
    ) 

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    # def __str__(self) -> str:
    #     return self.city + " " + self.state + " > > " + self.country