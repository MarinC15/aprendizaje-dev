# utils/guardado.py
"""
Módulo de guardado y utilidades de resultados.
Contiene:
- guardar_resultado(texto, nombre_reto, nombre_archivo)
- mostrar_y_guardar(texto, nombre_reto)
- mostrar_resultados_guardados(nombre_archivo)
- limpiar_resultados(nombre_archivo)
"""

import os
from datetime import datetime

# ruta por defecto dentro de la carpeta 'resultados'
DEFAULT_DIR = "resultados"
DEFAULT_FILE = "resultados.txt"

def _ruta_resultados(nombre_archivo=DEFAULT_FILE):
    """Devuelve la ruta completa asegurando que exista la carpeta resultados/"""
    os.makedirs(DEFAULT_DIR, exist_ok=True)
    return os.path.join(DEFAULT_DIR, nombre_archivo)

def guardar_resultado(texto, nombre_reto="Reto sin nombre", nombre_archivo=DEFAULT_FILE):
    """
    Guarda resultados con encabezado, fecha/hora y separador en resultados/resultados.txt.
    - texto: string con el contenido a guardar.
    - nombre_reto: título descriptivo del bloque.
    - nombre_archivo: nombre del archivo dentro de la carpeta 'resultados'.
    """
    ruta = _ruta_resultados(nombre_archivo)
    sello = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ruta, "a", encoding="utf-8") as f:
        f.write(f"\n=== {nombre_reto} ===\n")
        f.write(f"🕒 Fecha: {sello}\n\n")
        f.write(texto.rstrip() + "\n")
        f.write("-" * 30 + "\n")

def mostrar_y_guardar(texto, nombre_reto="Reto sin nombre", nombre_archivo=DEFAULT_FILE):
    """
    Muestra el texto en pantalla y pregunta al usuario si desea guardarlo.
    Si el usuario responde 's', guarda el contenido con guardar_resultado.
    """
    print(texto)
    opcion = input("¿Deseas guardar este resultado en el archivo? (s/n): ").strip().lower()
    while opcion not in ("s", "n"):
        opcion = input("Respuesta no válida. Escribe 's' para sí o 'n' para no: ").strip().lower()
    if opcion == "s":
        try:
            guardar_resultado(texto, nombre_reto, nombre_archivo)
            print("✅ Resultado guardado en resultados/{}.".format(nombre_archivo))
        except Exception as e:
            print(f"❌ Error al guardar: {e}")
    else:
        print("ℹ️ No se guardó el resultado.")

def mostrar_resultados_guardados(nombre_archivo=DEFAULT_FILE):
    """
    Muestra el contenido del archivo de resultados si existe, dentro de la carpeta resultados/.
    """
    ruta = _ruta_resultados(nombre_archivo)
    if not os.path.exists(ruta):
        print("\n⚠️ No hay resultados guardados todavía (archivo no encontrado).")
        return
    with open(ruta, "r", encoding="utf-8") as f:
        contenido = f.read()
    if contenido.strip() == "":
        print("\n📂 El archivo existe pero está vacío.")
    else:
        print("\n=== RESULTADOS GUARDADOS ===")
        print(contenido)

def limpiar_resultados(nombre_archivo=DEFAULT_FILE):
    """
    Limpia todo el contenido del archivo de resultados (sobrescribe).
    Deja una nota con la fecha en la parte superior.
    """
    ruta = _ruta_resultados(nombre_archivo)
    sello = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(f"=== Archivo limpiado ===\n")
        f.write(f"🕒 Fecha: {sello}\n")
        f.write("-" * 30 + "\n")
    print(f"✅ El archivo '{ruta}' ha sido limpiado.")
