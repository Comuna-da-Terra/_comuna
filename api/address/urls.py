from rest_framework.urls import path
from . import views

urlpatterns = [
    path("address/", view=views.AddressView.as_view()),
]
