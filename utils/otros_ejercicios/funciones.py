# funciones.py
# Ejemplos de funciones en Python

# 1️⃣ Definir una función simple
def saludar():
    """Muestra un saludo en consola"""
    print("¡Hola, bienvenido a la práctica con funciones!")

# 2️⃣ Función con parámetros
def presentar(nombre, edad):
    """Recibe un nombre y una edad, y los muestra"""
    print(f"Me llamo {nombre} y tengo {edad} años.")

# 3️⃣ Función con valor de retorno
def sumar(a, b):
    """Devuelve la suma de dos números"""
    return a + b

# 4️⃣ Función con valor por defecto
def saludar_persona(nombre="Invitado"):
    """Saluda a una persona, o usa un valor por defecto"""
    print(f"Hola, {nombre}!")

# 5️⃣ Función que usa *args (argumentos variables)
def listar_colores(*colores):
    """Muestra todos los colores recibidos"""
    print("Colores ingresados:")
    for color in colores:
        print("-", color)

# ---------------------------
# Ejecución de pruebas
# ---------------------------

saludar()

presentar("César", 21)

resultado = sumar(5, 7)
print("La suma de 5 y 7 es:", resultado)

saludar_persona()
saludar_persona("Laura")

listar_colores("rojo", "verde", "azul", "amarillo")
