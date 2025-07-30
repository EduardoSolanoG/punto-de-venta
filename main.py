# Importación de clases necesarias desde módulos externos
from cliente import Cliente
from producto import Producto
from venta import Venta

# Lista de productos disponibles (mientras tanto movida aquí desde el módulo producto)
lista_productos =[
        Producto("Galletas",18.5, 10),
        Producto("Yogurt", 15, 10),
        Producto("Gelatina", 7.5, 10),
        Producto("Papitas", 20, 10),
        Producto("Refresco", 10.5, 10)
    ]

# Función que muestra todos los productos disponibles con su precio y stock
def mostrar_productos(productos):
    print("\nProductos disponibles:")
    for i, prod in enumerate(lista_productos, start=1):
        print(f"{i}. {prod.get_nombreProducto()} - ${prod.get_precio()} ({prod.get_stock()} disponibles)")


# Función principal del programa
def main():
    print("=== Sistema de Punto de Venta ===")

    # Solicita el nombre del cliente y crea el objeto Cliente
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cliente = Cliente(nombre_cliente)

    # Crea una nueva venta asociada al cliente
    venta = Venta(cliente)

    # Ciclo principal para agregar productos al carrito
    while True:
        # Muestra los productos disponibles
        mostrar_productos(lista_productos)
        try:
            # Solicita al usuario que seleccione un producto por número
            opcion = int(input("Seleccione el número del producto que desea agregar: "))
            if 1 <= opcion <= len(lista_productos):
                producto = lista_productos[opcion - 1]

                # Solicita la cantidad del producto
                cantidad = int(input(f"Ingrese la cantidad de '{producto.get_nombreProducto()}': "))

                # Verifica que la cantidad sea válida y haya suficiente stock
                if cantidad > 0 and cantidad <= producto.get_stock():
                    producto.disminuir_stock(cantidad)
                    venta.agregar_producto(producto, cantidad)
                    print(f"{cantidad} unidades de '{producto.get_nombreProducto()}' agregadas al carrito.")
                else:
                    print("Cantidad inválida o stock insuficiente.")
            else:
                print("Opción fuera de rango.")
        except ValueError:
            print("Debe ingresar un número válido.")

        # Pregunta si desea seguir comprando, eliminar o finalizar
        continuar = input("¿Desea agregar otro producto? (s = sí, e = eliminar del carrito, n = no): ").lower()

        # Si desea eliminar un producto del carrito
        if continuar == 'e':
            if len(venta._Venta__productos) == 0:
                print("No hay productos en el carrito.")
            else:

                # Muestra los productos en el carrito para elegir cuál eliminar
                print("\nProductos en el carrito:")
                for i, (prod, cant) in enumerate(venta._Venta__productos):
                    print(f"{i + 1}. {prod.get_nombreProducto()} - {cant} unidades")

                try:
                    indice = int(input("¿Cuál producto deseas modificar? (escribe su número): ")) - 1
                    venta.eliminar_producto(indice)
                except ValueError:
                    print("Entrada inválida.")

        # Si responde algo diferente a 's', termina el ciclo
        elif continuar != 's':
            break

    # Muestra la factura o nota de venta
    venta.mostrar_nota()
    print("¡Gracias por su compra!")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
