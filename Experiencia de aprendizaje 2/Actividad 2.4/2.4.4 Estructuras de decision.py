contadorpasaje = 1
totalingresos = 0

while True:
    try:
        cantidaddepasajes = int(input("Cuantos pasajes deseas vender?: "))
        break
    except ValueError:
        print("Ingrese un numero valido. ")

for i in range(cantidaddepasajes):
    while True:
        try:
            valordelpasaje = int(input(f"Ingrese el valor del {contadorpasaje} pasaje: "))
            contadorpasaje += 1
            totalingresos += valordelpasaje
            break
        except ValueError:
            print("Ingrese un valor valido")

print("El precio de los pasajes es $",totalingresos)