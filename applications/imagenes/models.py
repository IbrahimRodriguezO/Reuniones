from django.db import models
from applications.reporte.models import Reporte
from .managers import ImagenManager
from model_utils.models import TimeFramedModel

# Create your models here.
class Imagenes(TimeFramedModel):
    reunion = models.ForeignKey(
        Reporte,
        on_delete=models.CASCADE,
        related_name="imagenes"
    )
    image = models.ImageField(verbose_name="Imagen", upload_to="reunion")

    objects = ImagenManager()

    def __str__(self):
        return f"{self.reunion}"