def suma_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("Las matrices deben tener la misma dimensión para sumarse.")
    
    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz1[0])):
            fila_resultado.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila_resultado)
    
    return resultado

def multiplicacion_matriz_escalar(matriz, escalar):
    resultado = []
    for i in range(len(matriz)):
        fila_resultado = []
        for j in range(len(matriz[0])):
            fila_resultado.append(matriz[i][j] * escalar)
        resultado.append(fila_resultado)
    
    return resultado

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def main():
    while True:
        print("\nMenú:")
        print("1. Sumar matrices")
        print("2. Multiplicar matriz por escalar")
        print("3. Salir")

        try:
            opcion = int(input("Ingrese la opción deseada: "))

            if opcion == 1:
                fila = int(input("Ingrese el número de filas de las matrices: "))
                columna = int(input("Ingrese el número de columnas de las matrices: "))
                
                matriz1 = [[int(input(f"Ingrese el elemento ({i+1},{j+1}) de la matriz 1: ")) for j in range(columna)] for i in range(fila)]
                matriz2 = [[int(input(f"Ingrese el elemento ({i+1},{j+1}) de la matriz 2: ")) for j in range(columna)] for i in range(fila)]

                resultado = suma_matrices(matriz1, matriz2)
                print("\nResultado de la suma:")
                imprimir_matriz(resultado)

            elif opcion == 2:
                fila = int(input("Ingrese el número de filas de la matriz: "))
                columna = int(input("Ingrese el número de columnas de la matriz: "))
                
                matriz = [[int(input(f"Ingrese el elemento ({i+1},{j+1}) de la matriz: ")) for j in range(columna)] for i in range(fila)]
                escalar = int(input("Ingrese el valor del escalar: "))

                resultado = multiplicacion_matriz_escalar(matriz, escalar)
                print("\nResultado de la multiplicación por escalar:")
                imprimir_matriz(resultado)

            elif opcion == 3:
                print("¡Hasta luego!")
                break

            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")

        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
