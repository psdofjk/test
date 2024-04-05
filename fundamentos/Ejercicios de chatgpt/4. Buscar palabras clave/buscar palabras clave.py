def buscar_palabras_clave(texto,palabra_clave):
    with open(texto,"r") as archivo:
        for numero_de_linea, linea in enumerate(archivo,start=1):
                print(numero_de_linea, linea)
                for palabra in palabra_clave:
                    if palabra.lower() in linea.lower():
                        return print(f"linea {numero_de_linea}: {linea.strip()}")
texto = "texto.txt"
palabra_clave = [i for i in input("ingrese una palabra: ")]
buscar_palabras_clave(texto,palabra_clave)