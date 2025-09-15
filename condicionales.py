# condicionales.py
# Ejemplo de condicionales en Python

# Pedimos un número al usuario
numero = int(input("Ingresa un número: "))

# Revisamos si es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")

# condicionales.py
# Ejemplos de condicionales en Python

edad = 20

# 1️⃣ Condicional simple
if edad >= 18:
    print("Eres mayor de edad.")

# 2️⃣ Condicional con else
if edad >= 18:
    print("Puedes votar.")
else:
    print("No puedes votar aún.")

# 3️⃣ Condicional con elif
nota = 3.5
if nota >= 4.5:
    print("Excelente 😃")
elif nota >= 3.0:
    print("Aprobado 🙂")
else:
    print("Reprobado 😢")

# 4️⃣ Condiciones compuestas con and / or
usuario = "admin"
contraseña = "1234"

if usuario == "admin" and contraseña == "1234":
    print("Acceso concedido ✅")
else:
    print("Acceso denegado ❌")
