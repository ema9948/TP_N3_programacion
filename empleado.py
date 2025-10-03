class Empleado:
    ESTADO_ALTA = "ALTA"
    ESTADO_BAJA = "BAJA"

    def __init__(self, nombre, apellido, sueldo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sueldo = sueldo
        self.__legajo = None
        self.__estado = Empleado.ESTADO_ALTA

    def get_legajo(self):
        return self.__legajo

    def get_estado(self):
        return self.__estado

    def __eq__(self, other):
        return self.__legajo == other.__legajo

    def __str__(self):
        return f"Empleado {self.__legajo}: {self.__nombre} {self.__apellido}, Sueldo: {self.__sueldo}, Estado: {self.__estado}"
