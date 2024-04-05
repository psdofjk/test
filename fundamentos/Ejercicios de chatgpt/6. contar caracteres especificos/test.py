caracteres = [input("Que caracter buscas?: ") for i in range(int(input("Cuantos caracteres?: ")))]

caracteres = {indice: input(f"{indice+1} caracter: ") for indice in range(int(input("¿Cuántos caracteres buscas?: ")))}
print(caracteres)

caracteres = {caracter: 0 for caracter in [input("Que caracter buscas?: ") for _ in range(int(input("Cuantos caracteres?: ")))]}

print(caracteres)
