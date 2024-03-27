deuda = 100000


while True:
    opcion = int(input("BIENVENIDO AL AUTOSERVICIO DE LA TOLAR\n1.PAGAR EL CUPO DE LA TARJETA DE CREDITO\n2.NUEVA COMPRA\n3.SALIR\nQue desea hacer?: "))
    if opcion > 3 and opcion < 1:
        continue

    elif opcion == 1:
        print(f"su deuda es de ${deuda}")
        pago = int(input("cuanto desea pagar?: "))
        while True:
            if pago > deuda:
                pago = int(input("Solo puede pagar un monto igual o menor: "))
            elif pago < 0:
                pago = int(input("no puede pagar numeros negativos: "))       
            else:
                break
        deuda = deuda - pago
        print(f"su nuevo saldo es de {deuda}")
        break
    
    elif opcion == 2:
        compras = int(print("bienvenido al simulador de compras, cuantas compras desea hacer?: "))
        for i in range(compras):


        