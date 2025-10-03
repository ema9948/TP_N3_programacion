# Trabajo Práctico N°3 – Asociación y Dependencia
Programación II – 2025 – 2do Cuatrimestre  
Tecnicatura Universitaria en Desarrollo Web

---

## Archivos incluidos

- **producto.py** → Clase `Producto` (identificada por nombre)
- **empleado.py** → Clase `Empleado` (identificado por legajo, con estados ALTA/BAJA)
- **empresa.py** → Clase `Empresa` (identificada por razón social, contiene empleados y productos)
- **main.py** → Archivo principal con las pruebas pedidas

---

## Ejercicios resueltos (Sección B)

1. Clase **Producto** creada con atributos privados y métodos `__init__`, `__str__` y `__eq__`.  
2. Clase **Empleado** creada con atributos privados y métodos `__init__`, `__str__` y `__eq__`.  
   - El constructor asigna estado **ALTA** por defecto.  
3. Clase **Empresa** creada con atributos privados y métodos pedidos:  
   - `altaEmpleado()` asigna legajo nuevo y agrega el empleado.  
   - `bajaEmpleado()` cambia estado a **BAJA** sin eliminarlo.  
   - `obtenerEmpleadosDeAlta()` devuelve solo los empleados en ALTA.  
   - `obtenerEmpleadoHistorico()` devuelve todos los empleados.  
   - `altaProducto()` agrega productos evitando duplicados.  
   - `__str__` imprime detalle de productos y empleados en ALTA.  
4. En `main.py` se crean 2 empresas, cada una con 3 empleados y 2 productos.  
   - Luego se dan de baja 2 empleados en una de las empresas.  
   - Finalmente, se imprime la información de cada empresa.  

---

## Ejecución
En una terminal, ejecutar:

```bash
python main.py
