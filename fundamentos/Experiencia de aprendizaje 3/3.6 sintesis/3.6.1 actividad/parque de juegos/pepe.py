# Abrir el archivo en modo de escritura ('w')
with open("archivo.txt", "w") as archivo:
    # Ciclo para escribir en el archivo
    while True:
        # Solicitar al usuario que escriba una línea
        linea = input("Escribe una línea (o escribe 'fin' para terminar): ")
        # Si el usuario escribe 'fin', salir del bucle
        if linea.lower() == 'fin':
            break
        # Escribir la línea en el archivo
        archivo.write(linea + "\n")

print("Se ha terminado de escribir en el archivo.")