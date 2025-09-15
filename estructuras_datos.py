# estructuras_datos.py
# Ejemplos básicos de estructuras de datos en Python

# 1️⃣ LISTAS: ordenadas y modificables
frutas = ["manzana", "banana", "cereza"]
print("Lista inicial:", frutas)

frutas.append("naranja")  # agregar
print("Después de append:", frutas)

frutas[1] = "kiwi"  # modificar
print("Después de modificar índice 1:", frutas)

print("Elemento en índice 0:", frutas[0])  # acceso

# 2️⃣ TUPLAS: ordenadas pero inmutables
coordenada = (10, 20)
print("Tupla:", coordenada)
# coordenada[0] = 15  # ❌ esto daría error

# 3️⃣ DICCIONARIOS: pares clave-valor
persona = {"nombre": "César", "edad": 21, "ciudad": "Medellín"}
print("Diccionario:", persona)
print("Nombre:", persona["nombre"])

persona["edad"] = 22  # actualizar
persona["profesion"] = "Estudiante"  # agregar
print("Diccionario actualizado:", persona)

# 4️⃣ CONJUNTOS: no ordenados, sin elementos repetidos
numeros = {1, 2, 3, 3, 4, 5}
print("Conjunto:", numeros)  # el 3 repetido desaparece

numeros.add(6)
print("Después de add:", numeros)
