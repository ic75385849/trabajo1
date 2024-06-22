import random
import string

def generar_contrasena():
    caracteres = string.ascii_letters + string.digits  # Letras mayúsculas, minúsculas y dígitos
    contrasena = ''.join(random.choice(caracteres) for _ in range(8))
    return contrasena

# Función principal para ejecutar el programa
def main():
    print("Generador de contraseñas de 8 caracteres (letras y números)")
    contrasena_generada = generar_contrasena()
    print(f"Tu contraseña generada es: {contrasena_generada}")

if __name__ == "__main__":
    main()
