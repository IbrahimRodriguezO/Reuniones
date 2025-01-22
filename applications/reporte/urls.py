from django.urls import path
from . import views

app_name = "reporte_app"

urlpatterns = [
    path(
        "add-reporte/",
        views.ReporteCreateView.as_view(),
        name="add-reporte"
    ),
    path(
        "opciones/<pk>/",
        views.ListaReporte.as_view(),
        name="opciones"
    ),
    path(
        "lista-reportes/",
        views.ListaReportesAdmin.as_view(),
        name="lista-reportes"
    ),
    path(
        "detalle-reporte/<pk>",
        views.DetalleReporteAdmin.as_view(),
        name="detalle-reporte"
    ),
    path(
        "listar-reportes/<pk>",
        views.ListaReportePDF.as_view(),
        name="listar-reportes"
    ),
]