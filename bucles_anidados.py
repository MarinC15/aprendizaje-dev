

# ==========================
# Ejemplo: cuadrícula 3x3
# ==========================

def ejemplo_cuadricula():
    for fila in range(1, 4):       # Recorre filas
        for columna in range(1, 4):  # Recorre columnas
            print(f"({fila},{columna})", end="  ")
        print()  # Salto de línea después de cada fila


# ==========================
# Reto 1: Cuadrado de asteriscos
# ==========================

def cuadrado_asteriscos(tamano=5):
    for fila in range(tamano):
        for columna in range(tamano):
            print("*", end=" ")
        print()

# ==========================
# Reto 2: Triángulo de asteriscos
# ==========================

def triangulo_asteriscos(tamano=5):
    for fila in range(1, tamano + 1):  # Desde 1 hasta 'tamano'
        for columna in range(fila):    # Número de * depende de la fila
            print("*", end=" ")
        print()  # Salto de línea después de cada fila
# ==========================
# Reto 3: Pirámide centrada de asteriscos
# ==========================

def piramide_asteriscos(tamano=5):
    for fila in range(1, tamano + 1):  
        # Espacios en blanco (se reduce a medida que avanzamos)
        print(" " * (tamano - fila), end="")  
        # Asteriscos (crecen con la fila: fórmula 2*fila - 1)
        print("*" * (2 * fila - 1))

# ==========================
# Reto 4: Rombo de asteriscos
# ==========================

def rombo_asteriscos(tamano=5):
    # Parte superior (incluye la fila del medio)
    for fila in range(1, tamano + 1):
        print(" " * (tamano - fila), end="")
        print("*" * (2 * fila - 1))
    
    # Parte inferior (excluye la fila del medio para no repetirla)
    for fila in range(tamano - 1, 0, -1):
        print(" " * (tamano - fila), end="")
        print("*" * (2 * fila - 1))
        
# ==========================
# Reto 5: Tablero de ajedrez
# Crea un tablero de ajedrez de 8x8 usando bucles anidados.
# Usaremos "#" para las casillas negras y " " (espacio) para las blancas.
# ==========================

print("\nReto 5: Tablero de ajedrez 8x8\n")
def tablero_ajedrez():
    tamano = input("Ingresa el tamaño del tablero (ejemplo 8): ")

    # Validación de entrada: si no es número o es <= 0, ponemos por defecto 8
    if not tamano.isdigit() or int(tamano) <= 0:
        print("Entrada inválida. Usando tamaño por defecto: 8")
        tamano = 8
    else:
        tamano = int(tamano)

    # Generar el tablero
    for fila in range(tamano):  
        for columna in range(tamano):  
            if (fila + columna) % 2 == 0:
                print("□", end=" ")  # Casilla blanca
            else:
                print("■", end=" ")  # Casilla negra
        print()  # Salto de línea al terminar cada fila

def tablas_multiplicar():
    print("\nTablas de multiplicar del 1 al 10:\n")
    for numero in range(1, 11):  # Tablas del 1 al 10
        print(f"Tabla del {numero}:")
        print("-" * 15)
        for i in range(1, 11):   # Multiplicadores del 1 al 10
            print(f"{numero} x {i} = {numero * i}")
        print()  # Salto de línea entre tablas

# ==========================
# Reto 7: Triángulo numérico
# ==========================

def triangulo_numerico():
    tamano=int(input("\nIngresa el tamaño del triángulo numérico: "))
    print(f"\nTriángulo numérico de tamaño {tamano}:\n")
    for fila in range(1, tamano + 1):   # Cada fila
        for numero in range(1, fila + 1):  # Números de la fila
            print(numero, end=" ")
        print()  # Salto de línea al final de cada fila

# ==========================
# Reto 8: Pirámide numérica centrada
# ==========================

def piramide_numerica(tamano=5):
    for fila in range(1, tamano + 1):
        # Espacios antes de los números
        print(" " * (tamano - fila), end="")
        # Números de la fila
        for numero in range(1, fila + 1):
            print(numero, end=" ")
        print()  # Salto de línea

import random

# ==========================
# Reto 9: Sopa de números
# ==========================

def sopa_numeros(filas=5, columnas=5):
    # Generar cuadrícula aleatoria
    matriz = [[random.randint(1, 9) for _ in range(columnas)] for _ in range(filas)]
    
    print("\n=== SOPA DE NÚMEROS ===")
    for fila in matriz:
        for num in fila:
            print(num, end=" ")
        print()
    
    # Usuario busca un número
    numero = int(input("\n¿Qué número deseas buscar (1-9)? "))
    
    encontrado = False
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == numero:
                print(f"✅ Número {numero} encontrado en posición ({i+1}, {j+1})")
                encontrado = True
    if not encontrado:
        print(f"❌ Número {numero} no está en la sopa.")

# ==========================
# Reto 10: Piedra, papel o tijera
# ==========================

def piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    print("\n=== JUEGO: PIEDRA, PAPEL O TIJERA ===")
    
    while True:
        jugador = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()
        
        if jugador == "salir":
            print("👋 Gracias por jugar.")
            break
        if jugador not in opciones:
            print("❌ Opción inválida, intenta de nuevo.")
            continue
        
        computadora = random.choice(opciones)
        print(f"La computadora eligió: {computadora}")
        
        if jugador == computadora:
            print("🤝 Empate.")
        elif (jugador == "piedra" and computadora == "tijera") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijera" and computadora == "papel"):
            print("🎉 ¡Ganaste!")
        else:
            print("😢 Perdiste.")

# ==========================
# Menú principal
# ==========================

def mostrar_menu():
    print("\n=== MENÚ DE RETOS DÍA 2 ===")
    print("1. Ejemplo cuadrícula 3x3")
    print("2. Cuadrado de asteriscos (5x5)")
    print("3. Triángulo de asteriscos")
    print("4. Pirámide centrada de asteriscos")
    print("5. Rombo de asteriscos")
    print("6. tablero de ajedrez")
    print("7. Tablas de multiplicar (1-10)")
    print("8. Triángulo numérico")
    print("9. Pirámide numérica centrada")
    print("10. Sopa de números")  
    print("11. Piedra, papel o tijera")
    print("0. Salir")


if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ")

        if opcion == "1":
            ejemplo_cuadricula()
        elif opcion == "2":
            cuadrado_asteriscos()
        elif opcion == "3":
            triangulo_asteriscos()
        elif opcion == "4":
            piramide_asteriscos()
        elif opcion == "5":
            rombo_asteriscos()
        elif opcion == "6":
            tablero_ajedrez()
        elif opcion == "7":
            tablas_multiplicar()
        elif opcion == "8":
            triangulo_numerico()
        elif opcion == "9":
            piramide_numerica()
        elif opcion == "10":
            sopa_numeros()
        elif opcion == "11":
            piedra_papel_tijera()


        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida, intenta de nuevo.")
