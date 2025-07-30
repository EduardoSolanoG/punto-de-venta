from cliente import Cliente
from producto import Producto
from venta import Venta

#Solo lo pase para no perder los datos y borrarlos del modulo producto
lista_productos =[
        Producto("Galletas",18.5, 10),
        Producto("Yogurt", 15, 10),
        Producto("Gelatina", 7.5, 10),
        Producto("Papitas", 20, 10),
        Producto("Refresco", 10.5, 10)
    ]

def mostrar_productos(productos):
    print("\nProductos disponibles:")
    for i, prod in enumerate(lista_productos, start=1):
        print(f"{i}. {prod.get_nombreProducto()} - ${prod.get_precio()} ({prod.get_stock()} disponibles)")



def main():
    print("=== Sistema de Punto de Venta ===")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cliente = Cliente(nombre_cliente)
    venta = Venta(cliente)

    while True:
        mostrar_productos(lista_productos)
        try:
            opcion = int(input("Seleccione el número del producto que desea agregar: "))
            if 1 <= opcion <= len(lista_productos):
                producto = lista_productos[opcion - 1]
                cantidad = int(input(f"Ingrese la cantidad de '{producto.get_nombreProducto()}': "))
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

        continuar = input("¿Desea agregar otro producto? (s = sí, e = eliminar del carrito, n = no): ").lower()
        if continuar == 'e':
            if len(venta._Venta__productos) == 0:
                print("No hay productos en el carrito.")
            else:
                print("\nProductos en el carrito:")
                for i, (prod, cant) in enumerate(venta._Venta__productos):
                    print(f"{i + 1}. {prod.get_nombreProducto()} - {cant} unidades")

                try:
                    indice = int(input("¿Cuál producto deseas modificar? (escribe su número): ")) - 1
                    venta.eliminar_producto(indice)
                except ValueError:
                    print("Entrada inválida.")
        elif continuar != 's':
            break
    venta.mostrar_nota()
    print("¡Gracias por su compra!")


if __name__ == "__main__":
    main()
