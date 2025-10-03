class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def __eq__(self, other):
        return self.__nombre == other.__nombre

    def __str__(self):
        return f"Producto: {self.__nombre}, Precio: {self.__precio}"
