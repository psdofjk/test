import csv

with open("ejemplo.txt", "r") as archivo:
    palabras = archivo.read().split()
    for palabra in palabras:
        if palabra[-1] == ".":
            palabras.remove(palabra)
    palabras_unicas = set(palabras)
    cantidad = len(palabras_unicas)


print(f"Hay {cantidad} palabras unicas, las que son:")
contador = 1
while contador < 20:
    for palabra in palabras_unicas:
            print(f"{contador}.", palabra)
            contador += 1
