# Iterar 5 veces
for i in range(5):
    # Abrir el archivo en modo escritura ('w')
    with open("archivo.txt", "w") as archivo:
        # Escribir en el archivo
        archivo.write(f"Escritura {i+1}\n")
    print(f"Se han escrito los datos en el archivo (iteración {i+1}).")

    # Abrir el archivo en modo lectura ('r')
    with open("archivo.txt", "r") as archivo:
        # Leer el contenido del archivo
        contenido = archivo.read()
    print(f"Contenido leído del archivo (iteración {i+1}):")
    print(contenido.strip())  # Eliminar caracteres de nueva línea al final

    print("-" * 30)  # Separador entre iteraciones
