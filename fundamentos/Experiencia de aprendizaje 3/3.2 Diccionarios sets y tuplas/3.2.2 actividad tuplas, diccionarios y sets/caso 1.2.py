lista = []
for i in range(3):
    lista.append(input(f"ingrese el {i+1} nombre: "))
print(lista)

longitudes = []
for i in lista:
    longitudes.append(len(i))
print(longitudes)

longitudmaslarga = max(longitudes)
print(longitudmaslarga)

ubicacionmaslarga = []
for i,j in enumerate(lista):
    if len(j) == longitudmaslarga:
        ubicacionmaslarga.append(i)
print(ubicacionmaslarga)