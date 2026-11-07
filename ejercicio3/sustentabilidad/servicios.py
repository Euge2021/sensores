def calcular_emisiones_carbono(
    consumo_kwh,
    factor_emision=0.4
):
    """
    Calcula las emisiones de carbono.

    El factor de emisión predeterminado es 0.4.
    """

    if consumo_kwh < 0:
        raise ValueError(
            "El consumo no puede ser negativo."
        )

    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros):

    emisiones_totales = 0
    consumo_por_planta = {}

    for registro in registros:

        planta = registro["planta"]
        consumo = registro["consumo_kwh"]

        emisiones = calcular_emisiones_carbono(consumo)

        emisiones_totales += emisiones

        if planta not in consumo_por_planta:
            consumo_por_planta[planta] = 0

        consumo_por_planta[planta] += consumo

    if consumo_por_planta:

        planta_mayor_consumo = max(
            consumo_por_planta,
            key=consumo_por_planta.get
        )

        consumo_maximo = consumo_por_planta[
            planta_mayor_consumo
        ]

    else:
        planta_mayor_consumo = None
        consumo_maximo = 0

    detalle_plantas = []

    for planta, consumo in consumo_por_planta.items():

        detalle_plantas.append({
            "planta": planta,
            "consumo_kwh": consumo,
            "emisiones_kg": calcular_emisiones_carbono(consumo)
        })

    return {
        "emisiones_totales": round(emisiones_totales, 2),
        "planta_mayor_consumo": planta_mayor_consumo,
        "consumo_maximo": consumo_maximo,
        "detalle_plantas": detalle_plantas,
        "cantidad_plantas": len(consumo_por_planta)
    }