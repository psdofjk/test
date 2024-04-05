
def menu():
    print("**************************")
    print("*                        *")
    print("*    Creativos . CL      *")
    print("*                        *")
    print("**************************\n")

    print("******************************************")
    print("*      Ingrese una opcion                *")
    print("*   1.Comprar entradas.                  *")
    print("*   2.Mostrar Ubicaciones disponibles.   *")
    print("*   3.Ver listado de asistentes.         *")
    print("*   4.Mostrar ganancias totales.         *")
    print("*              5.Salir.                  *")
    print("******************************************\n")

def comprar_entradas(matriz):
    contadorsilver = 0
    contadorgold = 0
    contadorplatinum = 0
    count = 0
    cantidad_entradas = int(input("Ingrese la cantidad de entradas a comprar: "))
    if cantidad_entradas >= 0 and cantidad_entradas <= 3:
        mostrar_disponibles(matriz)
        while count < cantidad_entradas:
            print("\nComprar entradas:\n")
            print("1. Platinum, $120.000 (Asientos del 1 al 20)")
            print("2. Gold, $80.000 (Asientos del 21 al 50)")
            print("3. Silver, $50.000 (Asientos del 51 al 100)")
            opcion_entrada = int(input("\nIngrese opcion (1=Platinum, 2=Gold, 3=Silver): \n"))

            if opcion_entrada == 1:
                listado_disponiblesPlatinum(matriz)
                posicionadorMatriz(matriz)
                contadorplatinum += 1
            elif opcion_entrada == 2:
                listado_disponibleGold(matriz)
                posicionadorMatriz(matriz)
                contadorgold += 1
            elif opcion_entrada == 3:
                listado_disponibleSilver(matriz)
                posicionadorMatriz(matriz)
                contadorsilver += 1
            else:
                input("Presione Enter para continuar\n")
            count += 1
        else:
            input("Presione enter")
    ganancias(contadorsilver, contadorgold, contadorplatinum)
def mostrar_disponibles(matriz):

    print("\nEscenario y asientos disponibles: \n")

    contador = 1
    for fila in matriz:
        for columna in fila:
            if columna == "":
                print(contador, end=" ")
            else:
                print("X",end=" ")
            contador = contador + 1
        print("")

def listado_disponiblesPlatinum(matriz):
    print("\nEscenario y asientos disponibles PLATINUM: \n")
    contador = 1 # contador, servirá para colocar numeros en los espacios vacios mientras se repite el ciclo
    contadorFila = 0
    matrizPlatinum = matriz[0:2]
    for fila in matrizPlatinum: #recorrerá primero la fila 0 hasta la 2 que enrealidad sera la 1
        contadorFila = contadorFila + 1
        print(f"Fila nro.{contadorFila}  ",end=" ")
        for columna in fila: #recorrerá a continuacion las columnas comenzando con la 0
            if columna == "": #si está vacia 
                print(contador,end=" ") #imprimirá el n del contador por cada vuelta
            else:
                print("X",end=" ")
            contador = contador +1
        print("")

def listado_disponibleGold(matriz):
    contador = 21 # contador, servirá para colocar numeros en los espacios vacios mientras se repite el ciclo
    contadorFila = 2
    matrizPlatinum = matriz[2:5]
    for fila in matrizPlatinum: #recorrerá primero la fila 0 hasta la 2 que enrealidad sera la 1
        contadorFila = contadorFila + 1
        print(f"Fila nro.{contadorFila}  ",end=" ")
        for columna in fila: #recorrerá a continuacion las columnas comenzando con la 0
            if columna == "": #si está vacia 
                print(contador,end=" ") #imprimirá el n del contador por cada vuelta
            else:
                print("X",end=" ")
            contador = contador +1
        print("")

def listado_disponibleSilver(matriz):
    contador = 51 # contador, servirá para colocar numeros en los espacios vacios mientras se repite el ciclo
    contadorFila = 5
    matrizPlatinum = matriz[5:11]
    for fila in matrizPlatinum: #recorrerá primero la fila 0 hasta la 2 que enrealidad sera la 1
        contadorFila = contadorFila + 1
        print(f"Fila nro.{contadorFila}  ",end=" ")
        for columna in fila: #recorrerá a continuacion las columnas comenzando con la 0
            if columna == "": #si está vacia 
                print(contador,end=" ") #imprimirá el n del contador por cada vuelta
            else:
                print("X",end=" ")
            contador = contador +1
        print("")

def posicionadorMatriz(matriz): #formula para calcular fila y columna con inputs

    nivel = int(input("\nIngrese la fila de asientos: "))-1 #tomará la fila mostrada en contradorFila y restará 1 para posicionarse correctamente en la matriz
    posicion = int(input("\nIngrese el numero de asiento: "))-1 #ingresará el numero del asento segun la fila

    #como estoy mostrando los asientos con sus decimales multiplicaré el nivel para luego restarlo con el numero de la columna
    #por ejemplo nivel = 5 - 1 fila4 * 10 tomará el rango de asientos - posicion quedará por ejemplo 44- 40 y eso dejará 4 que sería el n de columna 
    posicion = posicion - (nivel * 10) 

    if matriz[nivel][posicion] == "": #buscará la fila y columna especifica para comprobar si está vacia
                
        rut = int(input("Ingrese su RUT sin guin, puntos, ni digito verificador: "))
        matriz[nivel][posicion] = rut #reemplazara el valor vacio por el input de rut
        input("Asiento reservado correctamente, Presione Enter")
    else:
        input("Asiento ya reservado")

def listado_rut_asientos(matriz):
    print("Listado de asistentes")
    lista = matriz.flatten().tolist()
    for info_asiento in lista:
        if info_asiento != "":
            print(info_asiento)
    input("Presione enter para continuar")

def ganancias(contadorsilver,contadorgold,contadorplatinum):
    valorsilver = 50000
    valorgold = 80000
    valorplatinum = 120000
    print(f"  TIPO DE ENTRADA       CANTIDAD          TOTAL")
    print(f" Platinum $120.000      {contadorplatinum}                {contadorplatinum * valorplatinum}     ")
    print(f" Platinum $120.000      {contadorgold}                    {contadorgold * valorgold}         ")
    print(f" Platinum $120.000      {contadorsilver}                  {contadorsilver * valorsilver}       ")
    #profe no me salió mostrar el total, se me secó el cerebro :c
