usuarios = {"Juan":123,"pepe":333}

def iniciar_sesion():
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraeña: ")
    if usuario.lower in usuarios and contraseña.lower in usuarios.get(usuario): #esta parte del codigo deja entrar si la contraseña la tiene otro usuario
        print("Usuario ")
        

def registrar_usuarios():
    while True:
        nombre_de_usuario = input("Ingrese el nombre de su usuario: ")
        contraseña = input("Ingrese la contraseña: ")
        if nombre_de_usuario in usuarios:
            print("Ese usuario ya existe")
        else:
            usuarios[nombre_de_usuario] = contraseña
            opcion = input("Desea ingresar otro usuario? (si/no): ")
            if opcion == "si":
                print("Ok!")
                continue
            elif opcion == "no":
                print("Adios!")
                break
            else:
                print("Porfavor ingrese si o no")        


def usuarios_actuales():
    for i in usuarios.items():
        print(i)

print("Bienvenido al menú para registrar usuarios!\nQue desea?")
print("1. Iniciar sesión")
print("2. Registrar usuarios")
print("3. Eliminar usuarios")
print("4. Ver los usuarios actuales")
print("5. Salir")

while True:
    try:
        opcion = int(input("Elija una opción: "))
        if opcion == 1:
            iniciar_sesion()
        elif opcion == 2:
            registrar_usuarios()
        elif opcion == 3:
            eliminar_usuarios()
        elif opcion == 4:
            usuarios_actuales()
        elif opcion == 5:
            print("Adiós!")
            break
        else:
            print("Porfavor ingrese una opcion valida. ")

    except ValueError:
        print("Porfavor ingrese un numero valido") 