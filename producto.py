class Producto:
    def __init__(self, nombreP, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def get_nombre(self):
        return self.__nombre

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
        return f"{self.__nombre} - ${self.__precio} {self.__stock} disponible"