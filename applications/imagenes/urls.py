from django.urls import path
from . import views

app_name = "imagen_app"

urlpatterns = [
    path(
        "reunion/<pk>/imagenes/",
        views.agregar_imagenes,
        name="reunion_imagenes"
    ),
]