from collections import Counter

class Venta:
    def __init__(self, cliente):
        self.__cliente = cliente
        self.__productos = []  # lista de tuplas (producto, cantidad)

    def agregar_producto(self, producto, cantidad):
        self.__productos.append((producto, cantidad))

    def eliminar_producto(self, indice):
        try:
            if 0 <= indice < len(self.__productos):
                producto, cantidad_actual = self.__productos[indice]
                print(f"Tienes {cantidad_actual} piezas de {producto.get_nombre()} en el carrito.")
                opcion = input("¿Cuántas piezas deseas eliminar? (o escribe 'todo'): ")

                if opcion.lower() == 'todo':
                    producto.aumentar_stock(cantidad_actual)
                    self.__productos.pop(indice)
                    print("Producto eliminado completamente.")
                else:
                    cantidad = int(opcion)
                    if 0 < cantidad < cantidad_actual:
                        self.__productos[indice] = (producto, cantidad_actual - cantidad)
                        producto.aumentar_stock(cantidad)
                        print(f"Se eliminaron {cantidad} piezas.")
                    elif cantidad == cantidad_actual:
                        producto.aumentar_stock(cantidad)
                        self.__productos.pop(indice)
                        print("Producto eliminado completamente.")
                    else:
                        print("Cantidad inválida.")
            else:
                print("Índice fuera de rango.")
        except ValueError:
            print("Debes ingresar un número o la palabra 'todo'.")

    def mostrar_factura(self):
        print("\n=== FACTURA ===")
        print(f"Cliente: {self.__cliente.get_nombre()}")
        total = 0
        resumen = Counter()
        for producto, cantidad in self.__productos:
            resumen[producto.get_nombre()] += cantidad
            subtotal = producto.get_precio() * cantidad
            print(f"{producto.get_nombre()} x{cantidad} - ${subtotal}")
            total += subtotal
        print(f"Total a pagar: ${total}\n")

    def __str__(self):
        return f"Venta de {self.__cliente.get_nombre()} con {len(self.__productos)} productos."

