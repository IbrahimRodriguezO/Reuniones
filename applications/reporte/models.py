from django.db import models
from .managers import ReporteManager
from model_utils.models import TimeFramedModel

# Create your models here.
class Reporte(TimeFramedModel):
    dia = models.DateField(verbose_name="Día")
    hora = models.TimeField(verbose_name="Hora")
    tema = models.CharField(verbose_name="Tema", max_length=200)
    integrantes = models.TextField(verbose_name="Integrantes")
    lugar = models.CharField(verbose_name="Lugar", max_length=200)

    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"
        db_table = "reporte"

    objects = ReporteManager()

    def __str__(self):
        return f"{self.tema} - {self.dia}:{self.hora}"