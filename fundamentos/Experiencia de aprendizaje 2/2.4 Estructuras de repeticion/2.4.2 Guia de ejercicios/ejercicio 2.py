contadorbultoliviano = 0
contadorbultonormal = 0
contadorBultos = 1

while True:
    try:
        cantidadBultos = int(input("Ingrese la cantidad de bultos: "))
        break
    except ValueError:
        print("Ingrese un numero entero")

while contadorBultos <= cantidadBultos:
    while True:
        try:
            pesoBulto = int(input(f"Ingrese el peso (debe ser entre 1 a 10kg) del bulto {contadorBultos}: "))
            if pesoBulto >= 5 and pesoBulto <= 10:
                contadorbultonormal += 1
                contadorBultos +=1
                break
            elif pesoBulto >= 0 and pesoBulto < 5:
                contadorbultoliviano += 1
                contadorBultos += 1
                break
            else:
                print("EL peso debe estar entre 1 y 10kg")
        except ValueError:
            print("Ingrese un numero valido")


if pesoBulto >= 1 or pesoBulto <= 5:
    categoria = "liviana"
    if categoria == "liviana":
        Valor = 1000

if pesoBulto > 5 or pesoBulto <= 10:
    categoria = "normal"
    if categoria == "normal":
        Valor = 2000

if contadorbultoliviano > 0:
    print(f"Lleva {contadorbultoliviano} bultos livianos")

if contadorbultonormal > 0:
    print(f"Lleva {contadorbultonormal} bultos normales")

print(f"valor total a pagar {contadorbultoliviano * 1000 + contadorbultonormal * 2000}")