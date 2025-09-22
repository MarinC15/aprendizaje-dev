#!/usr/bin/env python3
"""
Archivo: bucles_anidados.py
Descripción: Colección de retos y ejemplos sobre bucles y bucles anidados.
Estructura: funciones de retos + utilidades (índice/menú) + main()
"""

import random
from datetime import datetime

# --------------------------
# Helpers / Utilidades
# --------------------------
def pedir_entero_positivo(prompt, default=None):
    """
    Pide un entero al usuario una vez. Si la entrada es vacía y se dio default, devuelve default.
    Si la entrada no es válida devuelve None (no repite en bucle para mantenerlo simple).
    """
    sufijo = f" (por defecto {default})" if default is not None else ""
    texto = input(f"{prompt}{sufijo}: ").strip()
    if texto == "":
        return default
    try:
        val = int(texto)
        if val <= 0:
            print("❌ El número debe ser mayor que 0.")
            return None
        return val
    except ValueError:
        print("❌ Entrada no válida. Se esperaba un número entero.")
        return None


def guardar_resultado(texto, nombre_archivo="resultados.txt"):
    """
    Guarda el texto en un archivo de resultados (modo append).
    """
    with open(nombre_archivo, "a", encoding="utf-8") as f:
        f.write(texto + "\n")


def mostrar_y_guardar(lineas, titulo, nombre_archivo="resultados.txt"):
    """
    Muestra en pantalla una lista de líneas y pregunta si se desea guardar.
    """
    print("\n".join(lineas))
    opcion = input("\n¿Deseas guardar este resultado en archivo? (s/n): ").strip().lower()
    if opcion == "s":
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bloque = [f"\n=== {titulo} ({fecha}) ==="]
        bloque.extend(lineas)
        guardar_resultado("\n".join(bloque), nombre_archivo)
        print("💾 Resultado guardado en archivo.")
    else:
        print("⚡ No se guardó el resultado.")


# --------------------------
# 1. FUNCIONES DE RETOS
# --------------------------

def ejemplo_cuadricula():
    resultado = ["Coordenadas de cuadrícula 3x3:"]
    for fila in range(1, 4):
        resultado.append("  ".join(f"({fila},{col})" for col in range(1, 4)))
    mostrar_y_guardar(resultado, "Ejemplo cuadrícula 3x3")


def cuadrado_asteriscos():
    tam = pedir_entero_positivo("Tamaño del cuadrado", default=5)
    if tam:
        resultado = ["Cuadrado de asteriscos:"]
        resultado.extend(["* " * tam for _ in range(tam)])
        mostrar_y_guardar(resultado, "Cuadrado de asteriscos")


def triangulo_asteriscos():
    tam = pedir_entero_positivo("Altura del triángulo", default=5)
    if tam:
        resultado = ["Triángulo de asteriscos:"]
        resultado.extend(["* " * fila for fila in range(1, tam + 1)])
        mostrar_y_guardar(resultado, "Triángulo de asteriscos")


def piramide_asteriscos():
    tam = pedir_entero_positivo("Altura de la pirámide", default=5)
    if tam:
        resultado = ["Pirámide centrada:"]
        for fila in range(1, tam + 1):
            espacios = " " * (tam - fila)
            resultado.append(espacios + ("* " * fila).rstrip())
        mostrar_y_guardar(resultado, "Pirámide centrada de asteriscos")


def rombo_asteriscos():
    tam = pedir_entero_positivo("Tamaño (filas de la mitad) del rombo", default=5)
    if tam:
        resultado = ["Rombo de asteriscos:"]
        for fila in range(1, tam + 1):
            espacios = " " * (tam - fila)
            resultado.append(espacios + ("* " * fila).rstrip())
        for fila in range(tam - 1, 0, -1):
            espacios = " " * (tam - fila)
            resultado.append(espacios + ("* " * fila).rstrip())
        mostrar_y_guardar(resultado, "Rombo de asteriscos")


def tablero_ajedrez():
    tam = pedir_entero_positivo("Tamaño del tablero", default=8)
    if tam:
        resultado = ["Tablero de ajedrez:"]
        for fila in range(tam):
            linea = []
            for col in range(tam):
                linea.append("□" if (fila + col) % 2 == 0 else "■")
            resultado.append(" ".join(linea))
        mostrar_y_guardar(resultado, "Tablero de ajedrez")


def tablas_multiplicar():
    resultado = ["Tablas de multiplicar del 1 al 10:"]
    for numero in range(1, 11):
        resultado.append(f"\nTabla del {numero}:")
        resultado.append("-" * 15)
        for i in range(1, 11):
            resultado.append(f"{numero} x {i} = {numero * i}")
    mostrar_y_guardar(resultado, "Tablas de multiplicar")


def triangulo_numerico():
    tam = pedir_entero_positivo("Tamaño del triángulo numérico", default=5)
    if tam:
        resultado = [f"Triángulo numérico de tamaño {tam}:"]
        for fila in range(1, tam + 1):
            resultado.append(" ".join(str(n) for n in range(1, fila + 1)))
        mostrar_y_guardar(resultado, "Triángulo numérico")


def piramide_numerica_centrada():
    try:
        filas = int(input("¿Cuántas filas quieres para la pirámide? ").strip())
        if filas <= 0:
            print("La cantidad debe ser mayor que 0.")
            return
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entero.")
        return

    resultado = ["Pirámide numérica centrada:"]
    for i in range(1, filas + 1):
        linea = " " * (filas - i)
        linea += "".join(str(j) for j in range(1, i + 1))
        linea += "".join(str(j) for j in range(i - 1, 0, -1))
        resultado.append(linea)
    mostrar_y_guardar(resultado, "Pirámide numérica centrada")


def sopa_numeros():
    filas = pedir_entero_positivo("Filas de la sopa", default=5)
    columnas = pedir_entero_positivo("Columnas de la sopa", default=5)
    if not filas or not columnas:
        return

    matriz = [[random.randint(1, 9) for _ in range(columnas)] for _ in range(filas)]
    resultado = ["Sopa de números:"]
    for fila in matriz:
        resultado.append(" ".join(str(n) for n in fila))

    try:
        numero = int(input("\n¿Qué número deseas buscar (1-9)? ").strip())
    except ValueError:
        print("Entrada inválida.")
        return
    if not (1 <= numero <= 9):
        print("Número fuera de rango.")
        return

    encontrado = False
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == numero:
                resultado.append(f"✅ Número {numero} encontrado en posición ({i+1}, {j+1})")
                encontrado = True
    if not encontrado:
        resultado.append(f"❌ Número {numero} no está en la sopa.")

    mostrar_y_guardar(resultado, "Sopa de números")


def piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    resultado = ["Juego: Piedra, papel o tijera"]
    while True:
        jugador = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").strip().lower()
        if jugador == "salir":
            resultado.append("👋 Gracias por jugar.")
            break
        if jugador not in opciones:
            print("❌ Opción inválida.")
            continue
        computadora = random.choice(opciones)
        resultado.append(f"Tú: {jugador} | PC: {computadora}")
        if jugador == computadora:
            resultado.append("🤝 Empate.")
        elif (jugador == "piedra" and computadora == "tijera") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijera" and computadora == "papel"):
            resultado.append("🎉 ¡Ganaste!")
        else:
            resultado.append("😢 Perdiste.")
    mostrar_y_guardar(resultado, "Piedra, papel o tijera")


def espiral_numerica():
    tam = pedir_entero_positivo("Tamaño de la espiral", default=4)
    if tam:
        matriz = [[0] * tam for _ in range(tam)]
        izquierda, derecha = 0, tam - 1
        arriba, abajo = 0, tam - 1
        num = 1

        while izquierda <= derecha and arriba <= abajo:
            for col in range(izquierda, derecha + 1):
                matriz[arriba][col] = num; num += 1
            arriba += 1
            for fila in range(arriba, abajo + 1):
                matriz[fila][derecha] = num; num += 1
            derecha -= 1
            if arriba <= abajo:
                for col in range(derecha, izquierda - 1, -1):
                    matriz[abajo][col] = num; num += 1
                abajo -= 1
            if izquierda <= derecha:
                for fila in range(abajo, arriba - 1, -1):
                    matriz[fila][izquierda] = num; num += 1
                izquierda += 1

        resultado = ["Espiral numérica:"]
        for fila in matriz:
            resultado.append(" ".join(str(x).rjust(3) for x in fila))
        mostrar_y_guardar(resultado, "Espiral numérica")


# --------------------------
# 2. ÍNDICE Y MENÚ
# --------------------------

def mostrar_indice():
    print("\n=== ÍNDICE GENERAL DE RETOS ===")
    print("1. Ejemplo cuadrícula 3x3 → Mostrar coordenadas de una cuadrícula.")
    print("2. Cuadrado de asteriscos → Dibuja un cuadrado con *.")
    print("3. Triángulo de asteriscos → Dibuja un triángulo creciente.")
    print("4. Pirámide centrada de asteriscos → Dibuja una pirámide simétrica.")
    print("5. Rombo de asteriscos → Figura completa con parte superior e inferior.")
    print("6. Tablero de ajedrez → Casillas □ y ■.")
    print("7. Tablas de multiplicar (1-10) → Muestra tablas completas.")
    print("8. Triángulo numérico → Números crecientes en filas.")
    print("9. Pirámide numérica centrada → Números en forma de pirámide.")
    print("10. Sopa de números → Matriz de números aleatorios.")
    print("11. Piedra, papel o tijera → Mini-juego contra la computadora.")
    print("12. Espiral numérica → Genera una matriz con números en espiral.")
    print("0. Salir")


def mostrar_menu():
    print("\n=== MENÚ DE RETOS DÍA 2 ===")
    print("1. Ejemplo cuadrícula 3x3")
    print("2. Cuadrado de asteriscos")
    print("3. Triángulo de asteriscos")
    print("4. Pirámide centrada de asteriscos")
    print("5. Rombo de asteriscos")
    print("6. Tablero de ajedrez")
    print("7. Tablas de multiplicar (1-10)")
    print("8. Triángulo numérico")
    print("9. Pirámide numérica centrada")
    print("10. Sopa de números")
    print("11. Piedra, papel o tijera")
    print("12. Espiral numérica")
    print("i. Ver índice de retos")
    print("0. Salir")


# --------------------------
# 3. MAIN (punto de entrada)
# --------------------------

def main():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ").strip().lower()

        if opcion == "1": ejemplo_cuadricula()
        elif opcion == "2": cuadrado_asteriscos()
        elif opcion == "3": triangulo_asteriscos()
        elif opcion == "4": piramide_asteriscos()
        elif opcion == "5": rombo_asteriscos()
        elif opcion == "6": tablero_ajedrez()
        elif opcion == "7": tablas_multiplicar()
        elif opcion == "8": triangulo_numerico()
        elif opcion == "9": piramide_numerica_centrada()
        elif opcion == "10": sopa_numeros()
        elif opcion == "11": piedra_papel_tijera()
        elif opcion == "12": espiral_numerica()
        elif opcion == "i": mostrar_indice()
        elif opcion == "0":
            print("¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
