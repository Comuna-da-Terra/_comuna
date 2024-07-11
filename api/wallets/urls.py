from rest_framework.urls import path
from . import views

urlpatterns = [
    path('wallet/',             view=views.WalletViews.as_view(), name="walllet"),    
    path('admin/wallets/',      view=views.AllWalletsView.as_view(), name="walllet")    
]
