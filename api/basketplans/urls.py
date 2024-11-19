from rest_framework.urls import path
from . import views

urlpatterns = [
    path("basketplan/", views.BasketPlanView.as_view()),
    path("basketplan/all/", views.ListAllBasketPlansView.as_view()),
    path("basketplan/edit/", views.EditBasketPlanView.as_view()),
    path("basketplan/delivery/", views.CreateDeliveriesView.as_view()),
]