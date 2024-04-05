def nombreapellido():
    nombres = []
    apellidos = []
    nombres_y_apellidos = []
    for i in range(3):
        nombres.append(input(f"Ingrese el {i+1}º nombre: "))
        apellidos.append(input(f"Ingrese el {i+1}º apellido: "))
        nombres_y_apellidos.insert(i,nombres[i] + " " + apellidos[i])
    for i in nombres_y_apellidos:
        print(i)

nombreapellido()
