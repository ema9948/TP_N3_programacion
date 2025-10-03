from empleado import Empleado

class Empresa:
    def __init__(self, razon_social):
        self.__razon_social = razon_social
        self.__productos = []
        self.__empleados = []

    def altaProducto(self, producto):
        for p in self.__productos:
            if p == producto:
                return
        self.__productos.append(producto)

    def altaEmpleado(self, empleado):
        max_legajo = 0
        for e in self.__empleados:
            if e.get_legajo() is not None and e.get_legajo() > max_legajo:
                max_legajo = e.get_legajo()
        empleado._Empleado__legajo = max_legajo + 1
        self.__empleados.append(empleado)

    def bajaEmpleado(self, empleado):
        for e in self.__empleados:
            if e == empleado:
                e._Empleado__estado = Empleado.ESTADO_BAJA

    def obtenerEmpleadosDeAlta(self):
        return [e for e in self.__empleados if e.get_estado() == Empleado.ESTADO_ALTA]

    def obtenerEmpleadoHistorico(self):
        return self.__empleados

    def __eq__(self, other):
        return self.__razon_social == other.__razon_social

    def __str__(self):
        texto = f"Empresa: {self.__razon_social}\n"
        texto += "Productos:\n"
        for p in self.__productos:
            texto += f"  - {p}\n"
        texto += "Empleados en ALTA:\n"
        for e in self.obtenerEmpleadosDeAlta():
            texto += f"  - {e}\n"
        return texto
