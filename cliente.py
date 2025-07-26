# Este modulo define la clase Cliente, que almacena el nombre de un cliente que hara una compra.
class Cliente:
    def __init__(self, nombre): #inicializa el atributo privado __nombre
        self.__nombre = nombre

    #Devuelve el nombre del cliente
    def get_nombre(self):
        return self.__nombre

    #Representacion en texto del cliente
    def __str__(self):
        return f"Cliente: {self.__nombre}"
