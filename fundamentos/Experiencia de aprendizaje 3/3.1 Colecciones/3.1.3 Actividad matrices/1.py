matriz = []

fila = 4
columnas = 3

for i in range(fila):
    fila = []
    for j in range(columnas):
        valor = (i + 1)* 3 + j + 1
        fila.append(valor)
    matriz.append(fila)

for fila in matriz:
    print(fila)

print("")

matriz2 = [[3,10,4,16],[1,7,8,-7],[9,-1,3,9]]

for i in matriz2:
    print(i)