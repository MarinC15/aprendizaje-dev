import random

# Ejemplo de bucle for
print("Ejemplo de bucle for con range:")

for i in range(1, 6):  # Va del 1 al 5
    print(f"Iteración número {i}")

# Ejemplo de bucle while
print("\nEjemplo de bucle while:")

contador = 1
while contador <= 5:
    print(f"Iteración número {contador}")
    contador += 1

"""3 mini-retos para practicar bien el tema de bucles"""
    
# Reto 1: Tabla de multiplicar con for
# Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10.    

numero = int(input("\nIngresa un número para ver su tabla de multiplicar: "))

print(f"\nTabla de multiplicar del {numero}:")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
    
# Reto 2: Suma de números pares con while
# Pide al usuario un número y calcula la suma de todos los números pares desde 1 hasta ese número.

limite = int(input("\nIngresa un número para sumar todos los números pares desde 1 hasta ese número: "))

suma_pares = 0
contador = 1
while contador <= limite:
    if contador % 2 == 0:
        suma_pares += contador
    contador += 1
print(f"\nLa suma de todos los números pares desde 1 hasta {limite} es: {suma_pares}")

# Reto 3: Contador con while

# Crea un programa que le pida al usuario un número inicial y un número final,
# y luego muestre todos los números entre esos dos valores.

num_inicial = int(input("\nIngresa un número inicial: "))
num_final = int(input("Ingresa un número final: "))

print(f"\nNúmeros entre {num_inicial} y {num_final}:")

contador = num_inicial
while contador <= num_final:
    print(contador)
    contador += 1

# Reto 4: Adivina el número (juego con while)

# El programa debe generar un número secreto entre 1 y 10,
# y el usuario tiene que adivinarlo. Se repite hasta que acierte.

numero_secreto = random.randint(1, 10)
adivinado = False
print("\nAdivina el número secreto entre 1 y 10.")

while not adivinado:
    intento = int(input("Ingresa tu intento: "))
    if intento == numero_secreto:
        adivinado = True
        print("🎉 ¡Correcto! Adivinaste el número.")
    else:
        print("❌ Incorrecto, intenta de nuevo.")
