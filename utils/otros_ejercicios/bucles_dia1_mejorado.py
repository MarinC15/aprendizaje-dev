import random

# ==========================
# Funciones de los retos
# ==========================

def ejemplo_for():
    print("\nEjemplo de bucle for con range:")
    for i in range(1, 6):  # Va del 1 al 5
        print(f"Iteración número {i}")


def ejemplo_while():
    print("\nEjemplo de bucle while:")
    contador = 1
    while contador <= 5:
        print(f"Iteración número {contador}")
        contador += 1


def tabla_multiplicar():
    numero = int(input("\nIngresa un número para ver su tabla de multiplicar: "))
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def suma_pares():
    limite = int(input("\nIngresa un número para sumar todos los números pares desde 1 hasta ese número: "))
    suma = 0
    contador = 1
    while contador <= limite:
        if contador % 2 == 0:
            suma += contador
        contador += 1
    print(f"\nLa suma de todos los números pares desde 1 hasta {limite} es: {suma}")


def contador_rango():
    num_inicial = int(input("\nIngresa un número inicial: "))
    num_final = int(input("Ingresa un número final: "))
    print(f"\nNúmeros entre {num_inicial} y {num_final}:")
    contador = num_inicial
    while contador <= num_final:
        print(contador)
        contador += 1


def adivina_numero():
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


print("==========================")
print("Menú principal")
print("==========================")

def mostrar_menu():
    print("\n=== MENÚ DE RETOS CON BUCLES ===")
    print("1. Ejemplo con for")
    print("2. Ejemplo con while")
    print("3. Tabla de multiplicar (for)")
    print("4. Suma de números pares (while)")
    print("5. Contador entre dos números (while)")
    print("6. Adivina el número (juego con while)")
    print("0. Salir")


if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ")

        if opcion == "1":
            ejemplo_for()
        elif opcion == "2":
            ejemplo_while()
        elif opcion == "3":
            tabla_multiplicar()
        elif opcion == "4":
            suma_pares()
        elif opcion == "5":
            contador_rango()
        elif opcion == "6":
            adivina_numero()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida, intenta de nuevo.")
# --- IGNORE ---
# ==========================