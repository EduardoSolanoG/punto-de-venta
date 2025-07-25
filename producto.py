class Producto:
    def __init__(self, nombreProducto, precio, stock):
        self.__nombreProducto = nombreProducto
        self.__precio = precio
        self.__stock = stock

    def get_nombreProducto(self):
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

    def __str__(self):
        return f"{self.__nombreProducto} - ${self.__precio} {self.__stock} disponible"


lista_productos =[
        Producto("Galletas",18.5, 10),
        Producto("Yogurt", 15, 10),
        Producto("Gelatina", 7.5, 10),
        Producto("Papitas", 20, 10),
        Producto("Refresco", 10.5, 10)
    ]

def mostrar_productos(productos):
    print("\nProductos disponibles:")
    for i, prod in enumerate(productos):
        print(f"{i + 1}. {prod.get_nombreProducto()} - ${prod.get_precio()} ({prod.get_stock()} disponibles)")
