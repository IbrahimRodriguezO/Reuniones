from django import forms
from .models import Reporte

class ReporteForm(forms.ModelForm):

    class Meta:
        model = Reporte
        fields = (
            "dia",
            "hora",
            "tema",
            "integrantes",
            "lugar",
        )
        widgets = {
            "dia": forms.DateInput(
                attrs={"type": "date"},  
                format="%Y-%m-%d"
            ),
            "hora": forms.TimeInput(
                attrs={"type": "time"},  
                format="%H:%M"
            ),
            "integrantes": forms.Textarea(
                attrs={
                    "rows": 5,  # Número de filas visibles
                    "cols": 40,  # Ancho del textarea
                    "style": "resize: none;",  # Bloquea la opción de cambiar tamaño
                }
            ),
        }