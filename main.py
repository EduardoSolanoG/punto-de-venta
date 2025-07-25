from cliente import Cliente
from producto import lista_productos, mostrar_productos


def main():
    print("=== Sistema de Punto de Venta ===")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cliente = Cliente(nombre_cliente)
    mostrar_productos(lista_productos)
    opcion = input("\nSeleccione el número del producto para agregar al carrito: ")


if __name__ == "__main__":
    main()
