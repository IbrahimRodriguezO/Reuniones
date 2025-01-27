from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, View
from .form import ReporteForm
from .models import Reporte
from .functions import render_to_pdf
from applications.imagenes.models import Imagenes

# Create your views here.
class ReporteCreateView(LoginRequiredMixin, CreateView):
    form_class = ReporteForm
    template_name = "reporte/add-reporte.html"
    login_url = reverse_lazy("users_app:user-login")
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect("imagen_app:reunion_imagenes", pk=self.object.pk)
    

class ListaReporte(LoginRequiredMixin, DetailView):
    model = Reporte
    template_name = "reporte/opciones.html"
    login_url = reverse_lazy("users_app:user-login")
    


class ListaReportesAdmin(LoginRequiredMixin, ListView):
    model = Reporte
    template_name = "reporte/lista-reportes.html"
    login_url = reverse_lazy("users_app:user-login")
    paginate_by = 10
    context_object_name = "reportes"
    ordering = ["-id"]
    

class DetalleReporteAdmin(LoginRequiredMixin, DetailView):
    model = Reporte
    template_name = "reporte/detalle.html"
    login_url = reverse_lazy("users_app:user-login")

        
    def get_context_data(self, **kwargs):
        context = super(DetalleReporteAdmin, self).get_context_data(**kwargs)
        pk = self.kwargs.get("pk")
        imagenes = Imagenes.objects.obtener_imagenes(pk=pk)

        context["imagenes"] = imagenes
        return context


class ListaReportePDF(View):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        reporte = Reporte.objects.obtener_reporte(pk=pk).first()
        
        if not reporte:
            return HttpResponse("Reporte no encontrado", status=404)

        # Las imágenes ya están prefetchadas
        imagenes = Imagenes.objects.obtener_imagenes(pk=pk)
        imagenes_url = [
            imagen.image.url if imagen.image else '' for imagen in imagenes
        ]

        integrantes = reporte.integrantes.split()
        print(integrantes)

        data = {
            "reporte": reporte,
            "imagenes": imagenes_url,
            "integrantes": integrantes,
            "base_url": "http://127.0.0.1:8000/"
        }
        
        # Renderizar PDF con las URLs absolutas
        pdf = render_to_pdf("reporte/lista.html", data)
        return HttpResponse(pdf, content_type="application/pdf")
