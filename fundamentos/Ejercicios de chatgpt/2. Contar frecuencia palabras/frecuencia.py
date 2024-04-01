import os

while True:
    print("1. Ingresar texto nuevo")
    print("2. Elegir otro texto")
    print("3. Salir")  
    try:
        opcion = int(input("Ingrese un valor: "))
        if opcion == 1:
            texto = str(input("Ingrese su texto: "))
            with open(texto,"+a") as archivo:
                x
        elif opcion == 2:
            x
        elif opcion == 3:
            print("Adiós!")
            break
        else:
            print("Ingrese un valor")
    except ValueError:
        print("elija un numero valido.")

with open("texto.txt","r") as archivo:
    palabras = archivo.read().split()
    print(palabras)
    frecuencia_palabras = {}
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    print(frecuencia_palabras)

for i in frecuencia_palabras:
    print(f"la palabra {i} se repite {frecuencia_palabras[i]} vez")