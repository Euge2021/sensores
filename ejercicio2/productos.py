from excepciones import StockInvalidoError


class DispositivoEcologico:

    def __init__(self, nombre, marca, precio, stock):

        self.nombre = nombre
        self.marca = marca
        self.precio = precio

        # Utilizamos el setter para validar el stock.
        self.stock = stock

    # Getter: permite consultar el stock.
    @property
    def stock(self):
        return self.__stock

    # Setter: permite modificar el stock con validación.
    @stock.setter
    def stock(self, nuevo_stock):

        if not isinstance(nuevo_stock, int) or isinstance(nuevo_stock, bool):
            raise StockInvalidoError("El stock debe ser un número entero.")

        if nuevo_stock < 0:
            raise StockInvalidoError("El stock no puede ser negativo.")

        self.__stock = nuevo_stock

    # Método para generar la ficha técnica.
    def ficha_tecnica(self):

        return (
            f"Producto: {self.nombre}\n"
            f"Marca: {self.marca}\n"
            f"Precio: ${self.precio}\n"
            f"Stock disponible: {self.stock}"
        )

    # Método para convertir el objeto en diccionario.
    def to_dict(self):

        return {
            "tipo": self.__class__.__name__,
            "nombre": self.nombre,
            "marca": self.marca,
            "precio": self.precio,
            "stock": self.stock
        }


class PanelSolar(DispositivoEcologico):

    def __init__(self, nombre, marca, precio, stock,
                 potencia_w, eficiencia):

        # Inicializamos los atributos de la clase padre.
        super().__init__(nombre, marca, precio, stock)

        # Atributos específicos del panel solar.
        self.potencia_w = potencia_w
        self.eficiencia = eficiencia

    # Sobrescribimos el método de la clase padre.
    def ficha_tecnica(self):

        return (
            f"{super().ficha_tecnica()}\n"
            f"Potencia: {self.potencia_w} W\n"
            f"Eficiencia: {self.eficiencia}%"
        )

    # Ampliamos los datos que se guardarán en JSON.
    def to_dict(self):

        datos = super().to_dict()

        datos["potencia_w"] = self.potencia_w
        datos["eficiencia"] = self.eficiencia

        return datos