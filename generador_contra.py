import random


def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'L', 'm', 'n', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
               ##simbolos = ['!', '#', '%', '&', '|', '?', '¡', '¿']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    caracteres = mayusculas + minusculas + numeros

    contrasena = []

    for i in range(15):
        caracteres_random = random.choice(caracteres)
        contrasena.append(caracteres_random)

    contrasena = "".join(contrasena) 
    return contrasena



def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena)


if __name__ == "__main__":
   run()