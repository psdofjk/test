contador = 1
try:
    solicitud = int(input("Ingrese un numero: "))
except ValueError:
    print("Porfavor ingrese un numero")
while contador <= solicitud:
    print(f"contador {contador}")
    if contador == solicitud:
        print("fin del proceso")
    contador += 1
