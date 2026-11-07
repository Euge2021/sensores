from django.shortcuts import render

from .datos import REGISTROS_CONSUMO

from .servicios import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):

    metricas = obtener_metricas_consumo(
        REGISTROS_CONSUMO
    )

    contexto = {
        "emisiones_totales": metricas["emisiones_totales"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "consumo_maximo": metricas["consumo_maximo"],
        "detalle_plantas": metricas["detalle_plantas"],
        "cantidad_plantas": metricas["cantidad_plantas"]
    }

    return render(
        request,
        "sustentabilidad/panel.html",
        contexto
    )