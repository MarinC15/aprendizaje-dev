# lambda_funciones.py
# Ejemplos de funciones anónimas (lambda) en Python

# 1️⃣ Una función lambda simple
cuadrado = lambda x: x * x
print("Cuadrado de 5:", cuadrado(5))

# 2️⃣ Función lambda con más de un parámetro
suma = lambda a, b: a + b
print("Suma de 3 + 7:", suma(3, 7))

# 3️⃣ Lambda dentro de una lista (útil en programación funcional)
operaciones = [
    lambda x: x + 1,    # suma 1
    lambda x: x * 2,    # multiplica por 2
    lambda x: x ** 2    # eleva al cuadrado
]

valor = 4
print("Operaciones sobre", valor, ":")
for op in operaciones:
    print(op(valor))
