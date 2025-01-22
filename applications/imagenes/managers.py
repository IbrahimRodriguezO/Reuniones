from django.db import models

class ImagenManager(models.Manager):
    
    def obtener_imagenes(self, pk):
        return self.filter(
            reunion=pk
        )
        