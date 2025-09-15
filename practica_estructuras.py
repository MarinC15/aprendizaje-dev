# practica_estructuras.py
# Ejercicios de práctica con estructuras de datos en Python

# 1️⃣ Listas: administrar una lista de tareas
tareas = ["estudiar", "hacer ejercicio", "leer"]
tareas.append("programar")  # agregar nueva tarea
tareas[1] = "correr"        # modificar tarea en índice 1
print("Lista de tareas:", tareas)

# 2️⃣ Tuplas: almacenar coordenadas y mostrarlas
punto = (4, 7)
print(f"Coordenada X: {punto[0]}, Y: {punto[1]}")

# 3️⃣ Diccionarios: representar información de un estudiante
estudiante = {
    "nombre": "César",
    "carrera": "Desarrollo de Software",
    "semestre": 6
}
estudiante["semestre"] = 7  # actualizar
estudiante["promedio"] = 4.2  # agregar
print("Diccionario estudiante:", estudiante)

# 4️⃣ Conjuntos: eliminar duplicados de una lista
numeros = [1, 2, 2, 3, 4, 4, 5]
sin_duplicados = set(numeros)
print("Números sin duplicados:", sin_duplicados)
