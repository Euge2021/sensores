import math
import re


def limpiar_registro_sensor(registro_raw):
    """Normaliza y devuelve un nuevo diccionario de sensor."""

    if not isinstance(registro_raw, dict):
        raise TypeError("El registro debe ser un diccionario.")

    # Identificador sin espacios sobrantes.
    sensor_id = str(registro_raw.get("sensor_id") or "").strip()

    if not sensor_id:
        sensor_id = "SENSOR-SIN-ID"

    # Temperatura numérica, admitiendo sufijos como C o °C.
    temperatura_raw = registro_raw.get("temperatura")

    if temperatura_raw is None:
        raise ValueError(f"Falta la temperatura del sensor {sensor_id}.")

    coincidencia = re.search(
        r"[-+]?(?:\d+(?:[.,]\d*)?|[.,]\d+)",
        str(temperatura_raw).strip(),
    )

    if not coincidencia:
        raise ValueError(
            f"Temperatura inválida para el sensor {sensor_id}: "
            f"{temperatura_raw!r}"
        )

    temperatura = float(coincidencia.group().replace(",", "."))

    if not math.isfinite(temperatura):
        raise ValueError(f"Temperatura inválida para el sensor {sensor_id}.")

    # Ubicación con valor por defecto si no existe o está vacía.
    ubicacion = str(registro_raw.get("ubicacion") or "").strip()

    if not ubicacion:
        ubicacion = "Ubicación no registrada"

    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion,
    }