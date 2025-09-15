# practica_funciones.py
# Ejercicios de práctica con funciones en Python

# 1️⃣ Función para calcular el área de un rectángulo
def area_rectangulo(base, altura):
    """Devuelve el área de un rectángulo"""
    return base * altura

# 2️⃣ Función para saber si un número es par o impar
def es_par(numero):
    """Devuelve True si el número es par, False si es impar"""
    return numero % 2 == 0

# 3️⃣ Función para convertir grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit"""
    return (celsius * 9/5) + 32

# ---------------------------
# Ejecución de pruebas
# ---------------------------

print("Área de rectángulo 5x3:", area_rectangulo(5, 3))

print("¿El número 10 es par?:", es_par(10))
print("¿El número 7 es par?:", es_par(7))

print("30°C equivalen a:", celsius_a_fahrenheit(30), "°F")
