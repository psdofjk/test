import os
import csv
from datetime import datetime

bitacora = []
def agregar_evento(evento):
    fecha_hora_actual = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    fecha_evento = f"{fecha_hora_actual} - {evento}"
    bitacora.append(fecha_evento)
    print(f"Evento '{evento}' registrado en la bitácora del auto.")

def seleccionar_archivo():
    carpeta_actual = os.getcwd()
    archivos = [archivo.name for archivo in os.scandir(carpeta_actual) if archivo.is_file()]

    print("Archivos en la carpeta actual:")
    for idx, archivo in enumerate(archivos):
            print(f"{idx + 1}: {archivo}")
        
    opcion = input("Seleccione el número de archivo que desea (o 'q' para salir): ")
    
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
        print("Opción inválida.")

def historico():
    if not bitacora:
        print("La bitácora está vacía.")
    else:
        print("Bitácora del auto:")
        for evento in bitacora:
            print(evento)

def guardar_registro_csv(nombre_archivo):
    try:
        with open(nombre_archivo, mode='w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(['Bitácora del Auto'])
            for evento in bitacora:
                writer.writerow([evento])
        print(f"Registro guardado en '{nombre_archivo}' con éxito.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}, coloque un nombre y extensión al archivo")

def menu():
    while True:
        print("\nMenú de registro historico de acciones en el Auto:")
        print("1. Agregar acción")
        print("2. Verificar historico")
        print("3. Guardar en archivo CSV")
        print("4. Cambiar de archivo")
        print("5. Salir")
        try:
            opcion = int(input("Ingrese la opción deseada: "))
            if opcion == 1:
                print("Escriba la acción (EJ: encender auto, viaje de Puerto Montt a Santiago")
                print("apagado auto, colocar alarma)")
                evento = input("Escriba la acción: ")
                agregar_evento(evento)
            elif opcion == 2:
                historico()
            elif opcion == 3:
                nombre_archivo = input("Ingrese el nombre del archivo CSV para guardar el registro ejemplo: 'bitacoraAuto.csv': ")
                guardar_registro_csv(nombre_archivo)
            elif opcion == 4:
                seleccionar_archivo()
            elif opcion == 5:
                print("saliendo de la bitácora")
                break
            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese un valor numérico válido.")
if __name__ == "__main__":
    menu()