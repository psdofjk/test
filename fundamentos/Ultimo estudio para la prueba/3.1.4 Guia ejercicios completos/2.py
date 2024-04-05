#listasuper
listaSuper = []
ValorSuper = []

print("Presione 1 para ingresar los productos del super")
print("Presione cualquier tecla para salir")
op = input("Seleccione opción: ")
if op == "1":
    while True:
        try:
            print("--------------------------------------------------------------")
            producto = input("Incorpore su producto, para salir presione 0: ")
            if producto != "0":
                listaSuper.append(producto)
                ValorSuper.append(int(input(f"Incorpore el valor del {producto}: ")))
                print("----Detalle boleta----")
                for i in range(len(listaSuper)):
                    print(f"{listaSuper[i]}: ${ValorSuper[i]}")
                total = sum(ValorSuper)
                print(f"El valor del total es de: ${total}")
                continue
            else:
                print("Adiós")
                break
        except:
            print("Ingreso erroneo")
else:
    print("Adiós")