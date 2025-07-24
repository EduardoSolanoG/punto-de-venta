class Producto:
    def __init__(self, nombreProducto, precio, stock):
        self.__nombreProducto = nombreProducto
        self.__precio = precio
        self.__stock = stock

    def get_nombre(self):
        return self.__nombreProducto

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    def disminuir_stock(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            return True
        return False

    def aunmentar_stock(self, cantidad):
        self.__stock += cantidad

    def __str__(self):
        return f"{self.__nombreProducto} - ${self.__precio} {self.__stock} disponible"