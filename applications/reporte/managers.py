from django.db import models

class ReporteManager(models.Manager):
    
    def obtener_reporte(self, pk=None):
        queryset = self.get_queryset().prefetch_related("imagenes")  # Usa el related_name definido en el modelo Imagenes
        if pk:
            return queryset.filter(pk=pk)
        return queryset