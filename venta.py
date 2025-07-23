from collections import Counter

class venta:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        self.__productos.append((producto, cantidad))

    def eliminar_prodcuto:
        try:
            if 0 <= indice < len(self.__productos)
                producto, cantidad_actual = self.productos[indice]
                print(f"Tienes {cantidad_actual} piezas de {producto.get_nombre()} en el carrito.")
                opcion = input("¿Cuántas piezas deseas eliminar? (o escribe 'todo'): ")

