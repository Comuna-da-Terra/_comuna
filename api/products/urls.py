from rest_framework.urls import path
from . import views

urlpatterns = [
    path("products/", view=views.ProductView.as_view(), name='products'),
    path("all_products/", view=views.ProductsListView.as_view(), name='products'),
    path("products/order/", view=views.ProductsInOrderAccountView.as_view(), name='products'),
    path("product/<uuid:pk>/", view=views.ProductDetailView.as_view(), name='product'),
    path("product/category/", view=views.CategoryView.as_view(), name='categories'),
]
