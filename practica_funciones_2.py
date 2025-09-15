# practica_funciones_2.py
# Segunda práctica con funciones en Python

# 1️⃣ Función que calcule el factorial de un número
def factorial(n):
    """Devuelve el factorial de un número entero n (n!)"""
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# 2️⃣ Función que determine si una palabra es un palíndromo
def es_palindromo(palabra):
    """Devuelve True si la palabra es un palíndromo, False si no lo es"""
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

# 3️⃣ Función que calcule el promedio de una lista de números
def promedio(lista):
    """Devuelve el promedio de una lista de números"""
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# ---------------------------
# Ejecución de pruebas
# ---------------------------

print("Factorial de 5:", factorial(5))
print("Factorial de 7:", factorial(7))

print("¿'radar' es palíndromo?:", es_palindromo("radar"))
print("¿'Python' es palíndromo?:", es_palindromo("Python"))

print("Promedio de [10, 20, 30, 40]:", promedio([10, 20, 30, 40]))
print("Promedio de lista vacía:", promedio([]))
