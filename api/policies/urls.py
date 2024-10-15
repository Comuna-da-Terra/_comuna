from rest_framework.urls import path
from . import views

urlpatterns = [
    path("policy/", view = views.PolicyView.as_view(), name=''),
]
