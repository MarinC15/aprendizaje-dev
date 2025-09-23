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


# -------------------------------
# Funciones de guardado
# -------------------------------
def guardar_resultado(texto, nombre_reto="Reto sin nombre", nombre_archivo="resultados.txt"):
    """Guarda resultados con encabezado, fecha/hora y separador."""
    with open(nombre_archivo, "a", encoding="utf-8") as f:
        f.write(f"\n=== {nombre_reto} ===\n")
        f.write(f"🕒 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(texto + "\n")
        f.write("-" * 30 + "\n")


def mostrar_y_guardar(texto, nombre_reto):
    """Muestra en pantalla y pregunta si guardar en archivo."""
    print(texto)
    opcion = input("¿Deseas guardar este resultado en el archivo? (s/n): ").strip().lower()
    if opcion == "s":
        guardar_resultado(texto, nombre_reto)
        print("✅ Resultado guardado en resultados.txt.")

def mostrar_resultados_guardados(nombre_archivo="resultados.txt"):
    """Muestra el contenido de resultados.txt si existe."""
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
        if contenido.strip() == "":
            print("\n📂 El archivo existe pero está vacío.")
        else:
            print("\n=== RESULTADOS GUARDADOS ===")
            print(contenido)
    except FileNotFoundError:
        print("\n⚠️ No hay resultados guardados todavía.")
        
def limpiar_resultados(nombre_archivo="resultados.txt"):
    """Limpia todo el contenido del archivo de resultados."""
    from datetime import datetime
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(f"=== Archivo limpiado ===\n")
        f.write(f"🕒 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("-" * 30 + "\n")
    print(f"✅ El archivo '{nombre_archivo}' ha sido limpiado.")

# --------------------------
# 1. FUNCIONES DE RETOS
# --------------------------

def ejemplo_cuadricula():
    """Ejemplo: imprimir coordenadas de una cuadrícula 3x3."""
    resultado = ""
    for fila in range(1, 4):
        for columna in range(1, 4):
            resultado += f"({fila},{columna})  "
        resultado += "\n"
    mostrar_y_guardar(resultado, "Reto 1: Ejemplo cuadrícula")


def cuadrado_asteriscos(tamano=None):
    """Reto 1: dibuja un cuadrado de asteriscos de tamaño NxN."""
    if tamano is None:
        tamano = pedir_entero_positivo("Tamaño del cuadrado", default=5)
        if tamano is None:
            return
    resultado = ""
    for _ in range(tamano):
        resultado += "* " * tamano + "\n"
    mostrar_y_guardar(resultado, "Reto 2: Cuadrado de asteriscos")


def triangulo_asteriscos(tamano=None):
    """Reto 2: triángulo rectángulo de asteriscos (creciente)."""
    if tamano is None:
        tamano = pedir_entero_positivo("Altura del triángulo", default=5)
        if tamano is None:
            return
    resultado = ""
    for fila in range(1, tamano + 1):
        resultado += "* " * fila + "\n"
    mostrar_y_guardar(resultado, "Reto 3: Triángulo de asteriscos")


def piramide_asteriscos(tamano=None):
    """Reto 3: pirámide centrada hecha con asteriscos."""
    if tamano is None:
        tamano = pedir_entero_positivo("Altura de la pirámide", default=5)
        if tamano is None:
            return
    resultado = ""
    for fila in range(1, tamano + 1):
        espacios = " " * (tamano - fila)
        resultado += espacios + ("* " * (fila)).rstrip() + "\n"
    mostrar_y_guardar(resultado, "Reto 4: Pirámide de asteriscos")


def rombo_asteriscos(tamano=None):
    """Reto 4: rombo formado por una pirámide superior e inferior."""
    if tamano is None:
        tamano = pedir_entero_positivo("Tamaño (filas de la mitad) del rombo", default=5)
        if tamano is None:
            return
    resultado = ""
    for fila in range(1, tamano + 1):
        espacios = " " * (tamano - fila)
        resultado += espacios + ("* " * fila).rstrip() + "\n"
    for fila in range(tamano - 1, 0, -1):
        espacios = " " * (tamano - fila)
        resultado += espacios + ("* " * fila).rstrip() + "\n"
    mostrar_y_guardar(resultado, "Reto 5: Rombo de asteriscos")


def tablero_ajedrez(tamano=None):
    """Reto 5: tablero de ajedrez dinámico. Usa □ y ■ para mostrar casillas."""
    if tamano is None:
        dato = pedir_entero_positivo("Ingresa el tamaño del tablero", default=8)
        if dato is None:
            return
        tamano = dato
    resultado = ""
    for fila in range(tamano):
        for columna in range(tamano):
            if (fila + columna) % 2 == 0:
                resultado += "□ "
            else:
                resultado += "■ "
        resultado += "\n"
    mostrar_y_guardar(resultado, "Reto 6: Tablero de ajedrez")


def tablas_multiplicar():
    """Muestra las tablas de multiplicar del 1 al 10."""
    resultado = "\nTablas de multiplicar del 1 al 10:\n\n"
    for numero in range(1, 11):
        resultado += f"Tabla del {numero}:\n"
        resultado += "-" * 15 + "\n"
        for i in range(1, 11):
            resultado += f"{numero} x {i} = {numero * i}\n"
        resultado += "\n"
    mostrar_y_guardar(resultado, "Reto 7: Tablas de multiplicar")


def triangulo_numerico(tamano=None):
    """Reto 7: triángulo numérico (1 / 1 2 / 1 2 3 ...)."""
    if tamano is None:
        tamano = pedir_entero_positivo("Ingresa el tamaño del triángulo numérico", default=5)
        if tamano is None:
            return
    resultado = f"\nTriángulo numérico de tamaño {tamano}:\n\n"
    for fila in range(1, tamano + 1):
        for numero in range(1, fila + 1):
            resultado += str(numero) + " "
        resultado += "\n"
    mostrar_y_guardar(resultado, "Reto 8: Triángulo numérico")


def piramide_numerica_centrada():
    """Reto 9: pirámide numérica centrada (palíndromo por fila)."""
    try:
        filas = int(input("¿Cuántas filas quieres para la pirámide? ").strip())
        if filas <= 0:
            print("La cantidad debe ser mayor que 0.")
            return
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entero.")
        return

    resultado = ""
    for i in range(1, filas + 1):
        resultado += " " * (filas - i)
        for j in range(1, i + 1):
            resultado += str(j)
        for j in range(i - 1, 0, -1):
            resultado += str(j)
        resultado += "\n"
    mostrar_y_guardar(resultado, "Reto 9: Pirámide numérica centrada")


def sopa_numeros(filas=None, columnas=None):
    """Reto 10: sopa de números. Genera una matriz y busca un número."""
    if filas is None:
        filas = pedir_entero_positivo("Filas de la sopa", default=5)
        if filas is None:
            return
    if columnas is None:
        columnas = pedir_entero_positivo("Columnas de la sopa", default=5)
        if columnas is None:
            return

    matriz = [[random.randint(1, 9) for _ in range(columnas)] for _ in range(filas)]
    resultado = "\n=== SOPA DE NÚMEROS ===\n"
    for fila in matriz:
        resultado += " ".join(str(n) for n in fila) + "\n"

    mostrar_y_guardar(resultado, "Reto 10: Sopa de números")


def piedra_papel_tijera():
    """Reto 11: juego contra la computadora."""
    opciones = ["piedra", "papel", "tijera"]
    resultado = "\n=== JUEGO: PIEDRA, PAPEL O TIJERA ===\n"
    while True:
        jugador = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").strip().lower()
        if jugador == "salir":
            print("👋 Gracias por jugar.")
            break
        if jugador not in opciones:
            print("❌ Opción inválida, intenta de nuevo.")
            continue
        computadora = random.choice(opciones)
        ronda = f"Tú: {jugador} | Computadora: {computadora}\n"
        if jugador == computadora:
            ronda += "🤝 Empate.\n"
        elif (jugador == "piedra" and computadora == "tijera") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijera" and computadora == "papel"):
            ronda += "🎉 ¡Ganaste!\n"
        else:
            ronda += "😢 Perdiste.\n"
        print(ronda)
        resultado += ronda
    mostrar_y_guardar(resultado, "Reto 11: Piedra, papel o tijera")


def espiral_numerica(tamano=None):
    """Reto 12: generar e imprimir una espiral numérica NxN."""
    if tamano is None:
        tamano = pedir_entero_positivo("Ingresa el tamaño de la espiral", default=4)
        if tamano is None:
            return

    matriz = [[0] * tamano for _ in range(tamano)]
    izquierda, derecha = 0, tamano - 1
    arriba, abajo = 0, tamano - 1
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

    resultado = "\n📌 Espiral numérica:\n"
    for fila in matriz:
        resultado += " ".join(str(x).rjust(3) for x in fila) + "\n"
    mostrar_y_guardar(resultado, "Reto 12: Espiral numérica")


# --------------------------
# 2. ÍNDICE Y MENÚ
# --------------------------
def mostrar_indice():
    """Muestra una descripción corta de cada reto (índice)."""
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
    """Muestra el menú principal."""
    print("\n=== MENÚ DE RETOS DÍA 2 ===")
    print("1. Ejemplo cuadrícula 3x3")
    print("2. Cuadrado de asteriscos (5x5)")
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
    print("r. Revisar resultados guardados")
    print("l. Limpiar archivo de resultados")
    print("0. Salir")


# --------------------------
# 3. MAIN (punto de entrada)
# --------------------------
def main():
    """Control principal del programa: bucle de menú."""
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ").strip().lower()

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
            piramide_numerica_centrada()
        elif opcion == "10":
            sopa_numeros()
        elif opcion == "11":
            piedra_papel_tijera()
        elif opcion == "12":
            espiral_numerica()
        elif opcion == "i":
            mostrar_indice()
        elif opcion == "r":
            mostrar_resultados_guardados()
        elif opcion == "l":
            limpiar_resultados()
        elif opcion == "0":
            print("¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
