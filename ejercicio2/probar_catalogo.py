from pathlib import Path

from catalogo.dominio.excepciones import StockInvalidoError
from catalogo.dominio.dispositivos import (
    DispositivoEcologico,
    PanelSolar
)
from catalogo.dominio.gestor import GestorInventario


def main():

    print("=== SISTEMA DE INVENTARIO ECOTECH ===")

    # Creamos un dispositivo ecológico
    dispositivo1 = DispositivoEcologico(
        "Lámpara LED",
        "EcoLight",
        15000,
        20
    )

    # Creamos un panel solar
    panel1 = PanelSolar(
        "Panel Solar 500W",
        "SolarTech",
        250000,
        10,
        0.5,
        95
    )

    # Probamos la excepción personalizada
    print("\n=== PRUEBA DE STOCK INVÁLIDO ===")

    try:

        dispositivo1.stock = -5

    except StockInvalidoError as error:

        print(f"Excepción controlada: {error}")

    # Mostramos las fichas técnicas
    print("\n=== FICHAS TÉCNICAS ===")

    lista_dispositivos = [
        dispositivo1,
        panel1
    ]

    for dispositivo in lista_dispositivos:

        print(dispositivo.ficha_tecnica())
        print("----------------------------")

    # Guardamos el catálogo en JSON
    ruta = Path(__file__).parent / "datos" / "catalogo_ecotech.json"

    GestorInventario.guardar_catalogo_json(
        lista_dispositivos,
        ruta
    )


if __name__ == "__main__":
    main()