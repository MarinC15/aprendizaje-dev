# funciones_orden_superior.py
# Ejemplos de map, filter y reduce en Python

from functools import reduce

# 1️⃣ MAP: aplicar una operación a cada elemento
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print("Cuadrados:", cuadrados)

# 2️⃣ FILTER: seleccionar elementos que cumplen condición
numeros = [10, 15, 20, 25, 30]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)

# 3️⃣ REDUCE: acumular valores de una lista
numeros = [1, 2, 3, 4, 5]
suma_total = reduce(lambda a, b: a + b, numeros)
print("Suma total:", suma_total)

# 4️⃣ Ejemplo combinado: sumar solo los pares al cuadrado
numeros = [1, 2, 3, 4, 5, 6]
resultado = reduce(
    lambda a, b: a + b,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, numeros))
)
print("Suma de cuadrados de pares:", resultado)
