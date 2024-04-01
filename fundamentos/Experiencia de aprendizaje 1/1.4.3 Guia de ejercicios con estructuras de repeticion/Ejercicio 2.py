def numero_al_cuadrado():
    inicio = 0
    try:
        ciclos = int(input("Cuantas veces desea usar la aplicacion?: "))
    except ValueError:
        print("Ingrese un numero entero")
               
    while inicio < ciclos:
        try:
            numero = float(input(f"Ingrese el {inicio+1} numero: "))
            numero_al_cuadrado = round(numero**2,2)
            print(f"el cuadrado de {numero} es: {numero_al_cuadrado}")
            inicio += 1
        except ValueError:
            print("Ingrese un numero")
    if inicio == ciclos:
        print("Adios!")

inicio = input("Desea usar la calculadora de numeros al cuadrado?: ")
if inicio == "si":
    numero_al_cuadrado()
else:
    print("Adios!")
    exit()