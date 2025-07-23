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

                if opcion.lower() == 'todo':
                   producto.aumentar_stock(cantidad_actual)
                   self.__productos.pop(indice)
                   print("Prodcuto eliminado completamente")
                else:
                    cantidad = int(opcion)
                    if 0 < cantidad < cantidad_actual:
                    self.__productos[indice] = (producto, cantidad_actual - cantidad)
                    producto.aunmentar_stock(cantidad)
                    print(f"Se eliminaron {cantidad} piezas.")
                elif cantidad == cantidad_actual:
                    producto.aunmentar_stock(cantidad)
                    self.__productos.pop(indice)
                    print("Producto eliminado completamente")
                else:
                print("cantidad invalida.")
            else:
                print("Indice fuera de rango.")
        except ValueError:
            print("Debes ingresar un número o palabra 'todo'.")
