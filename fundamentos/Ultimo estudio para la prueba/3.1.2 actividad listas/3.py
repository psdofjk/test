def añadirnombres():
    nombres = []
    contador = 0
    palabracorta = 100
    numeroborrar = ""
    while True:
        nombrecito = input(f"ingrese un nombre para añadirlo a la lista\nPara terminar ingrese 'no': ")
        if nombrecito.lower() == "no":
            print("Adiós!")
            break
        else:
            nombres.append(nombrecito)
            contador += 1
            if contador % 5 == 0:
                print("Eliminando el nombre más corto!")
                palabracorta = 100
                for i,j in enumerate(nombres):
                    if len(j) < palabracorta:
                        palabracorta = len(j)
                        numeroborrar = i
                print(f"Se ha eliminado '{nombres[numeroborrar]}'")
                nombres.remove(nombres[numeroborrar])
            print("Hasta ahora, esta es la lista de nombres:")
            for i in nombres:
                print(i)
            continue
añadirnombres()