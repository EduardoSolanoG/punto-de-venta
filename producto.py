#Este modulo define la clase producto, que representa un articulo a la venta con nombre, precio y cantidad disponible (stock)
class Producto:
    def __init__(self, nombreProducto, precio, stock): #inicializa los atributos privados del prodcuto
        self.__nombreProducto = nombreProducto         #Nombre del producto
        self.__precio = precio                         #Precio unitario
        self.__stock = stock                           #Cantidad en inventario

#Devuelve el nombre del producto
    def get_nombreProducto(self):
        return self.__nombreProducto

#Devuelve el precio del producto
    def get_precio(self):
        return self.__precio

#Devuelve el stock actual disponible
    def get_stock(self):
        return self.__stock

#Disminuye el stock si hay suficientes unidades
#Retorna True si fue posible, False si no hay suficiente stock
    def disminuir_stock(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            return True
        return False

#Aumenta el stock (por ejemplo, si el cliente se arrepiente de comprar algo)
    def aumentar_stock(self, cantidad):
        self.__stock += cantidad

#Representacion del producto como texto
    def __str__(self):
        return f"{self.__nombreProducto} - ${self.__precio} {self.__stock} disponible"
