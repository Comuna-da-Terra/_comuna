from rest_framework.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("account/", view=views.UserView.as_view()),
    path("account/<uuid:pk>/", view=views.UserDetailView.as_view()),
    path("login/", jwt_views.TokenObtainPairView.as_view()),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view()),
]
