# 🧩 Reto Integrador – Semana 1

# 📌 Enunciado:
# Crea un programa en Python que simule un pequeño sistema de registro de estudiantes.

# El programa debe:

# Pedir al usuario que ingrese el nombre de un estudiante.

# Pedir la nota final (un número entre 0 y 5).

# Usar una función para determinar si el estudiante aprueba o reprueba la materia (nota mínima aprobatoria = 3.0).

# Mostrar un mensaje personalizado con el resultado.



def evaluar_aprobacion(nombre, nota):
    """Determina si el estudiante aprueba o reprueba según la nota"""
    if nota < 0 or nota > 5:
        return "Nota inválida, ingrese una nota válida entre 0 y 5"
    elif nota >= 3.0:
        return f"¡Felicidades {nombre}! Has aprobado la materia con una nota de {nota}."
    else:
        return f"Lo siento {nombre}, has reprobado la materia con una nota de {nota}."

if __name__ == "__main__": 
    nom_estudiante = input("Ingresa el nombre del estudiante: ")
    nota_final = float(input("Ingresa la nota final (0-5): "))       

    resultado = evaluar_aprobacion(nom_estudiante, nota_final)
    print(resultado)
