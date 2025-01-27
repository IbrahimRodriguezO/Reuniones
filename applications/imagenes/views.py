from django.shortcuts import get_object_or_404, redirect, render
from .forms import ImagenFormSet
from .models import Reporte, Imagenes

def agregar_imagenes(request, pk):
    reporte = get_object_or_404(Reporte, pk=pk)
    
    if request.method == "POST":
        formset = ImagenFormSet(request.POST, request.FILES, queryset=Imagenes.objects.none())
        
        if formset.is_valid():
            for form in formset:
                # Guardar solo formularios que tengan una imagen cargada
                if form.cleaned_data.get('image'):
                    imagen = form.save(commit=False)
                    imagen.reunion = reporte  # Asociar la imagen al reporte
                    imagen.save()
            return redirect("reporte_app:opciones", pk=pk)

    else:
        formset = ImagenFormSet(queryset=Imagenes.objects.none())  # Formulario vacío para nuevas imágenes
    
    return render(request, "imagenes/subir-imagenes.html", {"formset": formset, "reporte": reporte})
