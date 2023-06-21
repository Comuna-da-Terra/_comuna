from rest_framework.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("accounts/", view=views.UserView.as_view()),
    path("account/", view=views.UserDetailView.as_view()),

    path("token/", jwt_views.TokenObtainPairView.as_view()),  # new
    path("token/refresh/", jwt_views.TokenRefreshView.as_view()),  # new  
]
