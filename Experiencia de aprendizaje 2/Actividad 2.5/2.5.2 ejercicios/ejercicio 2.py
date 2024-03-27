while True:
    print("1.ver mi saldo\n2.retirar\n3.salir")
    
    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion > 3 or opcion < 1:
            print("la opcion no es valida")
        else:
            print("la opcion es correcta")
            
    except ValueError:
        print("ingresee un numero valido")


    if opcion == 1 :
        while True:
            print("tiene un saldo de $500000")
            opcionval2 = int(input("presione 1 para ir atras o 2 para salir: "))
            if opcionval2 == 1:
                break
            elif opcionval2 == 2:
                print("cierre de sesión exitoso, adiós")
                break
            else:
                print("valor no aceptado")
                continue
            
        

    elif opcion == 2:
        while True:
            print("Transferencia realizada")
            opcionval2 = int(input("presione 1 para ir atras o 2 para salir: "))
            if opcionval2 == 1:
                break
            if opcionval2 == 2:
                print("cierre de sesión exioto, adiós")
                break
            else:
                print("valor no aceptado")    

    elif opcion == 3:
        print("cierre de sesión exitoso, adiós")
        break
