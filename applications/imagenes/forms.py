from django import forms
from django.forms import modelformset_factory
from .models import Imagenes

ImagenFormSet = modelformset_factory(
    Imagenes,
    fields=('image',),  # Solo el campo de imagen
    extra=4,             # Permitir 4 imágenes nuevas
    can_delete=False     # No permitir eliminar imágenes existentes
)