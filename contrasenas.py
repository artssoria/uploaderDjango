import string
import random

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ""
    for i in range (longitud):
        contrasena += random.choice(caracteres)
    return contrasena
longitud = int(input("cual es la longitud deseada de la contraseña: "))
nueva_contrasena = generar_contrasena(longitud)

print("la nueva contraseña es: ", nueva_contrasena)