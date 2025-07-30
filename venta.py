#Este modulo define la clase venta, que representa la compra de productos por parte de un cliente.
#Se pueden agregar productos, eliminarlos y mostrar una nota con el total

#para contar cuantas veces se compra cada producto
from collections import Counter

class Venta:
    def __init__(self, cliente): #Recibe un cliente y prepara una lista para almacenar los prodcutos comprados
        self.__cliente = cliente
        self.__productos = []  # lista de tuplas (producto, cantidad)

#Agrega un productocon su cantidad a la lista de compra
    def agregar_producto(self, producto, cantidad):
        self.__productos.append((producto, cantidad))

#Permite al cliente eliminar parte o todo un producto que ya habia agregado
    def eliminar_producto(self, indice):
        try:
            if 0 <= indice < len(self.__productos):
                producto, cantidad_actual = self.__productos[indice]
                print(f"Tienes {cantidad_actual} piezas de {producto.get_nombreProducto()} en el carrito.")
                opcion = input("¿Cuántas piezas deseas eliminar? (o escribe 'todo'): ")

                #Si se elimina todo, se repone el stock completo y se quita el prodcuto del carrito
                if opcion.lower() == 'todo':
                    producto.aumentar_stock(cantidad_actual)
                    self.__productos.pop(indice)
                    print("Producto eliminado completamente.")
                else:
                    cantidad = int(opcion)
                   #Se elimina una parte del total
                    if 0 < cantidad < cantidad_actual:
                        self.__productos[indice] = (producto, cantidad_actual - cantidad)
                        producto.aumentar_stock(cantidad)
                        print(f"Se eliminaron {cantidad} piezas.")
                   #Se elimina la cantidad exacta
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

#Muestra el resumen de compra: cliente, productos, cantidades y total
    def mostrar_nota(self):
        print("\n=== NOTA DE COMPRA ===")
        print(f"Cliente: {self.__cliente.get_nombre()}")
        total = 0
        resumen = Counter()
        print(f"PRODUCTO - CANTIDAD - SUBTOTAL")
        for producto, cantidad in self.__productos:
            resumen[producto.get_nombreProducto()] += cantidad
            subtotal = producto.get_precio() * cantidad
            print(f"{producto.get_nombreProducto()} x{cantidad} - ${subtotal}")
            total += subtotal
        print(f"TOTAL A PAGAR: ${total}\n")

#Representacion de la venta como texto
    def __str__(self): #revisenlo y diganme si esta bien este cambio
        return f"Compra de {self.__cliente.get_nombre()} con {len(self.__productos)} productos."