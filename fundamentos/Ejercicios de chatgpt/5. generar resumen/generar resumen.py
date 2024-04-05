class caracteres:
    def __init__(self, texto):
        self.texto = texto

    def cantidad_de_palabras(self):
        with open(texto,"r") as archivo:
            contador = 0
            texto_leido = archivo.read().strip()
            for i in texto_leido:
                contador += 1
        return print(f"el texto tiene {contador} palabras")

    def cantidad_de_lineas(texto):
        with open(texto,"r") as archivo:
            numero_de_lineas = sum(1 for linea in archivo if linea.strip())
        return print(f"{numero_de_lineas} lineas")

    def cantidad_de_caracteres(texto):
        with open(texto,"r") as archivo:
            texto_leido = archivo.read().strip()
            cantidad = 0
            for _ in enumerate(texto_leido, start=0):
                cantidad += len(texto_leido)
        return print(f"{cantidad} caracteres")

texto = caracteres("texto.txt")
texto.cantidad_de_caracteres(texto)
