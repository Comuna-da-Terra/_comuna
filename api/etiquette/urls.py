from  rest_framework.urls import path
from . import views

urlpatterns = [
    path("emitEtiquette/", view=views.EtiquetteView.as_view(), name="etiquette")
]