def listaa():
    lista = []
    numerito = 0
    palabra = ""
    for i in range(3):
        try:
            lista.append(str(input(f"ingrese el {i+1}º nombre: ")))
            for i,j in enumerate(lista):
                if len(j) > numerito:
                    numerito = len(j)
                    palabra = j
                    posicion = i + 1
        except ValueError:
            print("Ingrese un string valido")

    return print(f"la palabra más larga es {palabra}, es la {posicion}º y tiene {numerito} caracteres")

listaa()