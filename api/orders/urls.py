from rest_framework.urls import path
from . import views

urlpatterns = [
    path("order/product/", view = views.ProductOrderView.as_view(), name=''),
    path("order/product/delete/<uuid:pk>/", view  = views.ProductOrderDeleteView.as_view(),   name=''),
    path("order/product/update/<uuid:pk>/", view  = views.ProductOrderUpdateView.as_view(),   name=''),
    path("order/delete/<uuid:pk>/", view  = views.OrderDeleteView.as_view(),   name=''),
    path("order/updated/<uuid:pk>/", view  = views.OrderPartialUpdateView.as_view(),   name=''),
    path("order/active/", view  = views.OrderView.as_view(),   name=''),
    path("order/opens/", view  = views.DetailsOrderView.as_view(),   name=''),
    path("order/history/", view  = views.HistoryOrderView.as_view(),   name=''),
    path("orders/csv/", view  = views.ExportCSVOrders.as_view(),   name=''),
    
]
