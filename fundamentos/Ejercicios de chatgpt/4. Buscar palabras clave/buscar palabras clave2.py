# Definir las palabras clave que queremos buscar
palabras_clave = ["tecnológico", "inteligencia artificial", "IA", "automatización", "mercado laboral", "educación", "formación continua"]

# Función para verificar si una línea contiene alguna palabra clave
def contiene_palabra_clave(linea, palabras_clave):
    for palabra in palabras_clave:
        if palabra.lower() in linea.lower():  # Convertir ambas a minúsculas para hacer la comparación insensible a mayúsculas y minúsculas
            return True
    return False

# Leer el archivo de texto y buscar líneas que contengan palabras clave
archivo = "texto.txt"  # Nombre del archivo que contiene el texto
num_linea = 0  # Inicializamos el número de línea a 0
with open(archivo, "r") as archivo_texto:
    for linea in archivo_texto:
        num_linea += 1  # Incrementamos el número de línea antes de hacer la comprobación
        if contiene_palabra_clave(linea, palabras_clave):
            print(f"Línea {num_linea}: {linea.strip()}")  # Imprimir la línea y eliminar espacios en blanco al principio y al final
