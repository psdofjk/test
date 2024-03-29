import os

def seleccionar_archivo():
    while True:
        carpeta_actual = os.getcwd()
        archivos = [archivo.name for archivo in os.scandir(carpeta_actual) if archivo.is_file()]

        print("Archivos en la carpeta actual:")
        for idx, archivo in enumerate(archivos):
            print(f"{idx + 1}: {archivo}")
        
        opcion = input("Seleccione el número de archivo que desea (o 'q' para salir): ")

        if opcion.lower() == 'q':
            print("Saliendo del programa...")
            break

        try:
            opcion = int(opcion)
            if 1 <= opcion <= len(archivos):
                archivo_seleccionado = archivos[opcion - 1]
                ruta_completa = os.path.join(carpeta_actual, archivo_seleccionado)
                print(f"Archivo seleccionado: {archivo_seleccionado}")
                print(f"Ruta completa: {ruta_completa}")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número válido o 'q' para salir.")

seleccionar_archivo()
