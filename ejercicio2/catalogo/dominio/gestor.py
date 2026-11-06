import json
from pathlib import Path


class GestorInventario:

    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo):

        # Convertimos cada objeto en un diccionario
        catalogo = [
            dispositivo.to_dict()
            for dispositivo in lista_dispositivos
        ]

        # Convertimos la ruta en un objeto Path
        ruta = Path(ruta_archivo)

        # Creamos la carpeta si todavía no existe
        ruta.parent.mkdir(parents=True, exist_ok=True)

        # Guardamos los datos en formato JSON
        with ruta.open("w", encoding="utf-8") as archivo:

            json.dump(
                catalogo,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        print(f"Catálogo guardado correctamente en: {ruta}")