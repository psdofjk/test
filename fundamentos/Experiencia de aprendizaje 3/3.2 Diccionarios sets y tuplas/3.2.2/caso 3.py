nombres = []
longitudes = []
contador = 0
menor = 100
nombre = ""

while True:
    agregar = str(input("Desea ingresar otro nombre? (si/no): "))
    try:
        if agregar == "si":
            nombres.append(input("Ingrese un nombre: "))
            if len(nombres) % 5 == 0:
                for i in range(len(nombres)):
                    if len(nombres[i]) < menor:
                        nombre = nombres[i]
                nombres.remove(nombre)
            continue
        elif agregar == "no":
            print(nombres)
            break
    except ValueError:
        print("Porfavor ingrese un valor valido")

