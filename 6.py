import random
import string

def generar_contrasena():
    contrasena = ""
    caracteres = string.ascii_letters + string.digits 
    
    while len(contrasena) < 8:
        contrasena += random.choice(caracteres)
    
    return contrasena

def main():
    print("Generador de contraseñas de 8 caracteres")
    contrasena_generada = generar_contrasena()
    print(f"Tu contraseña generada es: {contrasena_generada}")

if __name__ == "__main__":
    main()
