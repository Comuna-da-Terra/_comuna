from rest_framework.urls import path
from . import views

urlpatterns = [
    path("order/product/", view = views.ProductOrderView.as_view(),         name=''),
    path("order/product/delete/<uuid:pk>/", view  = views.ProductOrderDeleteView.as_view(),   name=''),
    path("order/delete/<uuid:pk>/", view  = views.OrderDeleteView.as_view(),   name=''),
    
]
