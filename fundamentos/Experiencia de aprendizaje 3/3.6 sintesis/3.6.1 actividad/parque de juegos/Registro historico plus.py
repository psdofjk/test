import os
import csv
from datetime import datetime

fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

while True:
    print("Menú de registro historico de acciones en el auto")
    print("1. Ver los archivos guardados")
    print("2. Crear un archivo nuevo")
    print("3. Salir")

    try:
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1:
                carpeta_actual = os.getcwd()
                archivos = [archivo.name for archivo in os.scandir(carpeta_actual) if archivo.is_file()]
                if len(archivos) == 0:
                        print("No tiene archivos en la carpeta, desea crear uno nuevo? (si/no): ")
                        opcion = input()
                        if opcion == "si":
                            nombre_archivo = input("Que nombre le vas a dar al archivo?: ") + ".csv"
                            print(f"has creado {nombre_archivo}")
                            ruta_nuevo_archivo = os.path.join(carpeta_actual, nombre_archivo)
                            with open(ruta_nuevo_archivo, "w") as archivo:
                                registro = input("Que vas registar?: ")
                                archivo.write(f"{fecha_hora_actual}: {registro}\n" )
                            print(f"Se ha creado el nuevo archivo {ruta_nuevo_archivo}")
                            while True:
                                opcion = input("Deseas seguir escribiendo? (si/no): ")
                                if opcion == "si":
                                    registro = input("Que vas registar ahora?: ")
                                    archivo.write(f"{fecha_hora_actual}: {registro}\n" )
                                elif opcion == "no":
                                    break
                                else:
                                    print("Porfavor ingresa una opción valida")
                        elif opcion == "no":
                            break
                        else:
                            print("Porfavor ingrese una opción valida.")
                
                elif len(archivos) == 1:
                    print("solo tiene el archivo", archivos[0])
                    with open(archivos[0],"r") as archivo:
                        a = archivo.read()
                        print(a)
                    while True:    
                        registro = input("desea ingresar un nuevo registro? (si/no): ")
                        registro = registro.lower
                        if registro == "si":
                                with open(archivos[0], "w") as archivo:
                                    registro = input("Que deseas registrar?: ")
                                    archivos.write(f"{fecha_hora_actual}: {registro}\n" )
                                    while True:
                                        pregunta = input("Deseas registrar algo más? (si/no): ")
                                        pregunta = pregunta.lower
                                        if pregunta == "si":
                                            registro = input("Que deseas registrar?: ")
                                            archivos.write(f"{fecha_hora_actual}: {registro}\n" )
                                        elif pregunta == "no":
                                            print("Adios!")
                                            break
                                        else:
                                            print("Porfavor si o no")
                        elif registro == "no":
                            break
                        else:
                            print("Porfavor ingrese si o no")
                else:
                    print("archivos en la carpeta actual: ")
                    for i, j in enumerate(archivos):
                        print(f"{i + 1}: {j}")
                    try:
                        numero = int(input("Seleccione sobre que archivo desea sobreescribir: "))
                        if 1 <= numero <= len(archivos):
                            archivo_seleccionado = archivos[numero - 1]
                            ruta_completa = os.path.join(carpeta_actual, archivo_seleccionado)
                            print(f"Archivo seleccionado: {archivo_seleccionado}")
                            print(f"Ruta completa: {ruta_completa}\n")
                            print("Que deseas hacer?")
                            print("1. Escribir un registro nuevo")
                            print("2. Ver los anteriores")
                            print("3. salir")
                            opcion = input("Ingrese una opción: ")
                            if opcion == "1":
                                x
                            elif opcion == "2":
                                
                                opcion = input("Deseas ingresar un registro nuevo? (si/no): ")
                                if opcion == "si":
                                    with open(archivo_seleccionado,"w") as archivo:
                                        x
                                elif opcion == "no":
                                    x
                                else:
                                    print("Porfavor ingrese una opción valida")
                            elif opcion == "3":
                                print("Adiós!")
                                break
                            else:
                                print("Porfavor ingrese una opción valida")
                        else:
                            print("Opción invalida")
                    except ValueError:
                        print("Opción invalida")
            elif opcion == 2:
                nombre = input("Ingrese el nombre del archivo: ")
                print(f"Archivo guardado como el numero {i} de la carpeta {ruta_completa}")
            elif opcion == 3:
                print("Adiós!")
                break
            else:
                print("porfavor elija una opcion valida")
                continue
    except ValueError:
            print("Porfavor elija un numero")