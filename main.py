from empresa import Empresa
from empleado import Empleado
from producto import Producto


print(r"""
  ________                            ____  ___
 /  _____/______ __ ________   ____   \   \/  /
/   \  __\_  __ \  |  \____ \ /  _ \   \     / 
\    \_\  \  | \/  |  /  |_> >  <_> )  /     \ 
 \______  /__|  |____/|   __/ \____/  /___/\  \
        \/            |__|                  \_/  

              GRUPO X - TP3
""")


# Crear empresas
empresa1 = Empresa("WebSolutions S.A.")
empresa2 = Empresa("DataFactory S.R.L.")

# Crear productos
p1 = Producto("Hosting Basic", 1999)
p2 = Producto("Hosting Pro", 3499)
empresa1.altaProducto(p1)
empresa1.altaProducto(p2)

p3 = Producto("API Access", 4999)
p4 = Producto("Data Pipeline", 7999)
empresa2.altaProducto(p3)
empresa2.altaProducto(p4)

# Crear empleados
e1 = Empleado("Ana", "Gomez", 120000)
e2 = Empleado("Luis", "Martinez", 110000)
e3 = Empleado("Carla", "Perez", 125000)
empresa1.altaEmpleado(e1)
empresa1.altaEmpleado(e2)
empresa1.altaEmpleado(e3)

f1 = Empleado("Diego", "Ruiz", 100000)
f2 = Empleado("Mariana", "Lopez", 105000)
f3 = Empleado("Pablo", "Sosa", 98000)
empresa2.altaEmpleado(f1)
empresa2.altaEmpleado(f2)
empresa2.altaEmpleado(f3)

# Dar de baja empleados
empresa1.bajaEmpleado(e2)
empresa1.bajaEmpleado(e3)

# Mostrar resultados
print(empresa1)
print("=" * 40)
print(empresa2)
