from productos import DispositivoEcologico, PanelSolar
from excepciones import StockInvalidoError
from gestor_inventario import GestorInventario


def main():

    print("====================================")
    print("   ECOTECH SOLUTIONS")
    print("   SISTEMA DE INVENTARIO")
    print("====================================")

    # Creamos los productos válidos.
    panel1 = PanelSolar(
        "Panel Solar Residencial",
        "EcoSun",
        250000,
        15,
        450,
        21.5
    )

    panel2 = PanelSolar(
        "Panel Solar Industrial",
        "GreenPower",
        500000,
        8,
        600,
        23.5
    )

    dispositivo1 = DispositivoEcologico(
        "Lámpara LED",
        "EcoLight",
        15000,
        30
    )

    # Probamos la excepción personalizada.
    print("\n--- PRUEBA DE EXCEPCIONES ---")

    try:

        panel1.stock = -5

    except StockInvalidoError as error:

        print(f"Error controlado: {error}")

    # Mostramos las fichas técnicas.
    print("\n--- FICHAS TÉCNICAS ---")

    lista_dispositivos = [
        panel1,
        panel2,
        dispositivo1
    ]

    for dispositivo in lista_dispositivos:

        print("\n------------------------")
        print(dispositivo.ficha_tecnica())

    # Guardamos el catálogo JSON.
    print("\n--- PERSISTENCIA DEL CATÁLOGO ---")

    GestorInventario.guardar_catalogo_json(
        lista_dispositivos,
        "catalogo_ecotech.json"
    )


if __name__ == "__main__":
    main()