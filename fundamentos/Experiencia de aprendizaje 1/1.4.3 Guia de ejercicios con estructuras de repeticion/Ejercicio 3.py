try:
    num = float(input("Ingrese un numero: "))
except ValueError:
    print("elije un numero")

acumulador_total = 0
while num != 0:
    acumulador_total = num + acumulador_total
    print(f"Tu suma acumulativa es hasta el momento: {acumulador_total}")
    try:
        num = float(input("ingresa otro numero: "))
    except ValueError:
        print("Ingresa otro numero: ")
    print("si quieres salirte, apreta 0")
if num == 0:
    print("Adios!")
    exit()