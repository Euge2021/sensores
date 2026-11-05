import math


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    """Devuelve los IDs en alerta y el promedio de temperatura."""

    umbral = float(umbral_temperatura)

    if not math.isfinite(umbral):
        raise ValueError("El umbral debe ser un número válido.")

    sensores_alerta = []
    temperaturas = []

    for sensor in lista_sensores_limpios:
        if "sensor_id" not in sensor or "temperatura" not in sensor:
            raise ValueError(
                "Cada sensor debe incluir 'sensor_id' y 'temperatura'."
            )

        sensor_id = str(sensor["sensor_id"]).strip()
        temperatura = float(sensor["temperatura"])

        if not math.isfinite(temperatura):
            raise ValueError(f"Temperatura inválida para {sensor_id}.")

        temperaturas.append(temperatura)

        if temperatura > umbral:
            sensores_alerta.append(sensor_id)

    promedio = (
        sum(temperaturas) / len(temperaturas)
        if temperaturas
        else 0.0
    )

    return sensores_alerta, promedio