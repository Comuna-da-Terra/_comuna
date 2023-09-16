from rest_framework.urls import path
from . import views

urlpatterns = [
    path("account/address/", views.AddressView.as_view()),
    path("account/address/<uuid:pk>/", views.AddressDetailView.as_view()),
]
