from .excepciones import StockInvalidoError


class DispositivoEcologico:

    def __init__(self, nombre, marca, precio, stock):

        self.nombre = nombre
        self.marca = marca
        self.precio = precio

        # Utilizamos el atributo privado
        self.__stock = 0

        # Asignamos el stock mediante la propiedad
        self.stock = stock

    # Getter: permite consultar el stock
    @property
    def stock(self):
        return self.__stock

    # Setter: permite modificar el stock
    @stock.setter
    def stock(self, cantidad):

        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise TypeError("El stock debe ser un número entero.")

        if cantidad < 0:
            raise StockInvalidoError(
                "Error: el stock no puede ser negativo."
            )

        self.__stock = cantidad

    # Método para generar la ficha técnica
    def ficha_tecnica(self):

        return (
            f"Producto: {self.nombre}\n"
            f"Marca: {self.marca}\n"
            f"Precio: ${self.precio}\n"
            f"Stock disponible: {self.stock}"
        )

    # Método para convertir el objeto en diccionario
    def to_dict(self):

        return {
            "tipo": "DispositivoEcologico",
            "nombre": self.nombre,
            "marca": self.marca,
            "precio": self.precio,
            "stock": self.stock
        }


# Clase hija: hereda de DispositivoEcologico
class PanelSolar(DispositivoEcologico):

    def __init__(
        self,
        nombre,
        marca,
        precio,
        stock,
        potencia_kw,
        eficiencia
    ):

        # Inicializamos los atributos heredados
        super().__init__(nombre, marca, precio, stock)

        # Atributos específicos del panel solar
        self.potencia_kw = potencia_kw
        self.eficiencia = eficiencia

    # Polimorfismo: sobrescribimos el método heredado
    def ficha_tecnica(self):

        return (
            f"=== FICHA TÉCNICA: PANEL SOLAR ===\n"
            f"Producto: {self.nombre}\n"
            f"Marca: {self.marca}\n"
            f"Precio: ${self.precio}\n"
            f"Stock disponible: {self.stock}\n"
            f"Potencia: {self.potencia_kw} kW\n"
            f"Eficiencia: {self.eficiencia}%"
        )

    # Sobrescribimos la conversión a diccionario
    def to_dict(self):

        datos = super().to_dict()

        datos["tipo"] = "PanelSolar"
        datos["potencia_kw"] = self.potencia_kw
        datos["eficiencia"] = self.eficiencia

        return datos