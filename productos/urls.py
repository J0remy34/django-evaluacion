from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_productos, name="lista_productos"),
    path("informacion/", views.informacion_productos, name="informacion_productos"),
]
