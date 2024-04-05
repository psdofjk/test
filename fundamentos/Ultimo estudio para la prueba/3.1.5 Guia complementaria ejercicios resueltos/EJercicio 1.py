#Chile2030
Nombre = []
Direccion = []
Telefono = []
contador = 0
while contador < 30:
    contador += 1
    Nombre.append(input("Ingrese el nombre del alumno: "))
    Direccion.append(input("Ingrese la direccion del alumno: "))
    Telefono.append(input("Ingrese el telefono del alumno: "))
    agregar = input("Desea agregar otro alumno (s/n): ")
    if agregar == "s":
        for i in range(len(Nombre)):
            print(f"Nombre: {Nombre[i]}")
            print(f"Dirección: {Direccion[i]}")
            print(f"Telefono: {Telefono[i]}\n")
        continue
    elif agregar == "n":
        print("Adiós")
        for i in range(len(Nombre)):
            print(f"{i + 1}.-")
            print(f"Nombre: {Nombre[i]}")
            print(f"Dirección: {Direccion[i]}")
            print(f"Telefono: {Telefono[i]}\n")
        break