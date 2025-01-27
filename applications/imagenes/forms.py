from django import forms
from django.forms import modelformset_factory
from .models import Imagenes
from django.forms import BaseModelFormSet, ValidationError

class CustomImagenFormSet(BaseModelFormSet):
    def clean(self):
        """Ignorar formularios vacíos y validar que solo se envíen imágenes"""
        super().clean()
        valid_forms_count = 0  # Contador para validar el máximo de imágenes

        for form in self.forms:
            # Si el formulario no tiene datos y no está marcado para borrar, ignorarlo
            if not form.has_changed():
                continue
            
            # Validar si el campo 'image' está vacío
            if not form.cleaned_data.get('image'):
                raise ValidationError("Debe cargar una imagen en cada formulario utilizado.")

            valid_forms_count += 1

        # Validar si excedemos el máximo permitido (4 imágenes)
        if valid_forms_count > 4:
            raise ValidationError("No puedes subir más de 4 imágenes.")


ImagenFormSet = modelformset_factory(
    Imagenes,
    fields=('image',),  # Solo el campo de imagen
    extra=4,             # Permitir hasta 4 formularios
    can_delete=False,    # No permitir eliminar imágenes existentes
    formset=CustomImagenFormSet
)
