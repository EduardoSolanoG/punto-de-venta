from cliente import Cliente
from producto import lista_productos, mostrar_productos


def main():
    print("=== Sistema de Punto de Venta ===")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cliente = Cliente(nombre_cliente)
    mostrar_productos(lista_productos)
    opcion = input("\nSeleccione el número del producto para agregar al carrito: ")

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
    for i, prod in enumerate(productos):
        print(f"{i + 1}. {prod.get_nombreProducto()} - ${prod.get_precio()} ({prod.get_stock()} disponibles)")

if __name__ == "__main__":
    main()
