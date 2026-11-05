from sensors.services import (
    limpiar_registro_sensor,
    generar_resumen_sensores,
)


def main():
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
            "sensor_id": " SENSOR-003 ",
            "temperatura": "27,8 grados",
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

    print("=== Reporte de sensores EcoTech Solutions ===")
    print(f"Umbral: {umbral:.1f} °C")
    print(f"Promedio de la planta: {promedio:.2f} °C")

    if sensores_alerta:
        print("Sensores que superan el umbral:")
        for sensor_id in sensores_alerta:
            print(f"- {sensor_id}")
    else:
        print("No hay sensores que superen el umbral.")

    print("\nLecturas normalizadas:")
    for sensor in sensores_limpios:
        print(
            f"- {sensor['sensor_id']}: "
            f"{sensor['temperatura']:.1f} °C "
            f"({sensor['ubicacion']})"
        )


if __name__ == "__main__":
    main()