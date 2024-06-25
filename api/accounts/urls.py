from rest_framework.urls import path
from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("account/", view=views.ListUserView.as_view()),
    path("accounts/admin/", view=views.ListAllUserView.as_view()),
    path("account/register/", view=views.CreateUserView.as_view()),
    path("account/<uuid:pk>/", view=views.UserDetailView.as_view()),

    path('account/change-password/', view=views.PasswordChangeAPIView.as_view(), name='password_change_api'),

    path("auth/", jwt_views.TokenObtainPairView.as_view()),
    path("auth/refresh/", jwt_views.TokenRefreshView.as_view()),
    path("auth/verify/", views.TokenVerifyView.as_view()),

    #PasswordResetView: È responsável por apresentar um formulário para que possamos preencher o e-mail de recuperação.
#Ele também gerará um link único para a redefinição de senha
#caso o email não exista na base de dados ele simplesmente irá ignorar.
    path('account/reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
#PasswordResetDoneView:È a página mostrada depois que o usuário recebeu o link por e-mail para redifinir a senha.
#Que é template que irá mostrar que o e-mail foi enviado com sucesso.
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
#PasswordResetConfirmView: Esse método irá apresentar um formulário para inserir uma nova senha.
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
#PasswordResetCompleteView:È responsável por exibir ao usuário um template informando que a senha foi alterada com sucesso!
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password/password-reset-complete.html"), name="password_reset_complete"),
]
