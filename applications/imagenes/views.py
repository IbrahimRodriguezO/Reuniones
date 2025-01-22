from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImagenFormSet
from .models import Imagenes
from applications.reporte.models import Reporte

def agregar_imagenes(request, pk):
    reporte = get_object_or_404(Reporte, pk=pk)
    
    if request.method == "POST":
        formset = ImagenFormSet(request.POST, request.FILES, queryset=Imagenes.objects.none())  # No cargar imágenes existentes
        if formset.is_valid():
            for form in formset:
                imagen = form.save(commit=False)
                imagen.reunion = reporte  # Asociar la imagen al reporte
                imagen.save()
            return redirect("reporte_app:opciones", pk=pk)

    else:
        formset = ImagenFormSet(queryset=Imagenes.objects.none())  # Solo formularios vacíos
    
    return render(request, "imagenes/subir-imagenes.html", {"formset": formset, "reporte": reporte})

