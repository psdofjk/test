while True:
    opcion = input("Menú\n1. Sumar matrices\n2. Multiplicar matriz por escalar\n3. Salir\nIngrese la opción deseada: ")
    if opcion == "1":
        try:
            fila = int(input("Cuantas filas quieres?: "))
            columna = int(input("Cuantas columnas quieres?: "))

            matriz1 = [[int(input(f"matriz 1 ({i+1},{j+1}): ")) for j in range(columna)] for i in range(fila)] 
            matriz2 = [[int(input(f"matriz 2 ({i+1},{j+1}): ")) for j in range(columna)] for i in range(fila)]

            sumamatriz = []
            for i in range(fila):
                for j in range(columna):
                    sumamatriz.append(matriz1[i][j] + matriz2[i][j])
            for i in sumamatriz:
                print(i)
            
            continue
        except ValueError:
            print("porfavor solo use numeros")
    elif opcion == "2":
        try:
            fila = int(input("cuantas filas tiene su matriz?: "))
            columna  = int(input("cuantas columnas tiene su matriz?: "))

            matriz = [[int(input(f"{i+1},{j+1}): ")) for j in range(columna)] for i in range(fila)]
            escalar = int(input("por que valor desea multiplicar?: "))

            matrizmultiplicada = [] 
            for i in range(fila):
                for j in range(columna):
                    matrizmultiplicada.append(matriz[i][j] * escalar)
            print(matrizmultiplicada)
            continue
        except ValueError:
            print("Porfavor solo use numeros")
    elif opcion == "3":
        print("Adiós!")
        break
    else:
        print("Porfavor elija una opción valida")
        continue
    