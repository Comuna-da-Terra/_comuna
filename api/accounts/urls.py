from rest_framework.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("account/", view=views.ListUserView.as_view()),
    path("account/register/", view=views.CreateUserView.as_view()),
    path("account/<uuid:pk>/", view=views.UserDetailView.as_view()),

    path("auth/", jwt_views.TokenObtainPairView.as_view()),
    path("auth/refresh/", jwt_views.TokenRefreshView.as_view()),
    path("auth/verify/", views.TokenVerifyView.as_view()),
]
