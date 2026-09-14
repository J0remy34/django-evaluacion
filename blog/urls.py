from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio_blog, name="inicio_blog"),
    path("sobre/", views.sobre_blog, name="sobre_blog"),
]
