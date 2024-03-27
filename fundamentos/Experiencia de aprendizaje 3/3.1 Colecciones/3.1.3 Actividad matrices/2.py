matriz = [[["a","b","c"],["a","b","c"],["a","b","c"]],[["a","b","c"],["a","b","c"],["a","b","c"]],[["a","b","c"],["a","b","c"],["a","b","c"]]]

def contar(matriz,elemento):
    cantidad = 0
    for capa in matriz:
        for fila in capa:
            cantidad += fila.count(elemento)
    return print(cantidad)

cantidad_a = contar(matriz, "a")
