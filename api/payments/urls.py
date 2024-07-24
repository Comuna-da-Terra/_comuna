from rest_framework.urls import path
from . import views


urlpatterns = [
    path("payment/", view= views.PaymentView.as_view(), name="payment")
]