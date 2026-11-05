import json


class GestorInventario:

    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):

        try:

            # Convertimos los objetos en diccionarios.
            catalogo = [
                dispositivo.to_dict()
                for dispositivo in lista_dispositivos
            ]

            # Guardamos los datos en formato JSON.
            with open(ruta_archivo, "w", encoding="utf-8") as archivo:

                json.dump(
                    catalogo,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

            print("\nCatálogo guardado correctamente.")
            print(f"Archivo: {ruta_archivo}")

        except (OSError, TypeError, AttributeError) as error:

            print(f"Error al guardar el catálogo: {error}")