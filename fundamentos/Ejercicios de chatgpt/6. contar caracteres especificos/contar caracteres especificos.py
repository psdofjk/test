def contar_caracteres_especificos(texto):
        caracteres = {caracter: 0 for caracter in [input("Que caracter buscas?: ") for _ in range(int(input("Cuantos caracteres?: ")))]}
        with open(texto,"r") as archivo:
            contenido = archivo.read()
            for i in contenido:
                if i in caracteres:
                    caracteres[i] += 1
        return print(caracteres)
                        
texto = "texto.txt"
contar_caracteres_especificos(texto)

