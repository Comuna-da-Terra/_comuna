from rest_framework.urls import path
from . import views

urlpatterns = [
    path("order/product/", view=views.ProductOrderView.as_view(), name=''),
    path("order/detail/", view=views.ProductOrderDeleteView.as_view(), name=''),
    
]
