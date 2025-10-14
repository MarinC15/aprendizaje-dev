from utils.guardado import guardar_resultado

def pedir_numero(mensaje, tipo=float):
    """
    Solicita al usuario un número (int o float) con validación y registro de errores.
    Si el usuario ingresa un valor inválido, se guarda en el archivo de resultados.
    """
    while True:
        entrada = input(mensaje)
        try:
            valor = tipo(entrada)
            return valor
        except ValueError:
            error_msg = f"❌ Error: entrada no válida ('{entrada}') — esperaba tipo {tipo.__name__}"
            print(error_msg)
            guardar_resultado(error_msg)  # 👈 Guardamos también el error
