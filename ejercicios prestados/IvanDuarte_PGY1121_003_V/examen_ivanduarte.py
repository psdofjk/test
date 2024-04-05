import numpy as np
import funciones as fn
contadorplatinum = 0
contadorgold = 0
contadorsilver = 0
matriz = np.full((10,10),"", dtype=object)

while True:
    try:
        fn.menu()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            fn.comprar_entradas(matriz)
        elif opcion == 2:
            fn.mostrar_disponibles(matriz)
        elif opcion == 3:
            fn.listado_rut_asientos(matriz)
        elif opcion == 4:
            fn.ganancias(contadorsilver,contadorgold,contadorplatinum)
        elif opcion == 5:
            print("Programa finalizado (︶｡︶)zzZZ")
            print("*****IVAN ANDRES DUARTE HERRERA*****")
            print("*****15-07-2022*****")
            break
        else:
            print("Ingreso erroneo")
    except:
        print("Parametro erroneo")