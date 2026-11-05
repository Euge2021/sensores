from django.shortcuts import render

from sensors.services import (
    limpiar_registro_sensor,
    generar_resumen_sensores,
)


def reporte_sensores(request):
    registros_crudos = [
        {
            "sensor_id": " SENSOR-001 ",
            "temperatura": "24.5C",
            "ubicacion": "Planta Norte",
        },
        {
            "sensor_id": "SENSOR-002",
            "temperatura": "31.2 °C",
            "ubicacion": "Planta Sur",
        },
        {
            "sensor_id": "SENSOR-003",
            "temperatura": "27.8C",
        },
    ]

    sensores_limpios = [
        limpiar_registro_sensor(registro)
        for registro in registros_crudos
    ]

    umbral = 30.0

    sensores_alerta, promedio = generar_resumen_sensores(
        sensores_limpios,
        umbral,
    )

    contexto = {
        "lecturas": sensores_limpios,
        "sensores_alerta": sensores_alerta,
        "promedio": promedio,
        "umbral": umbral,
    }

    return render(request, "sensors/reporte.html", contexto)