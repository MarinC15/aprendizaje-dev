# bucles.py
# Ejemplos de bucles en Python

# FOR: mostrar los números del 1 al 10
print("Números del 1 al 10 con for:")
for i in range(1, 11):
    print(i, end=" ")
print("\n")  # salto de línea

# WHILE: sumar los números pares del 1 al 100
suma = 0
n = 1
while n <= 100:
    if n % 2 == 0:
        suma += n
    n += 1

print("La suma de los números pares del 1 al 100 es:", suma)
