# Caso 1: Nombre con Mayor Cantidad de Caracteres
nombres = []
for i in range(3):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)

nombre_largo = max(nombres, key=len)
print(f"El nombre con mayor cantidad de caracteres es: {nombre_largo}")
# Caso 2: Nombres y Apellidos Ordenados
nombres = ["Juan", "Ana", "Carlos"]
apellidos = ["Gomez", "Perez", "Rodriguez"]

# Ordenar y mostrar nombres
nombres.sort()
print("Nombres ordenados:", nombres)

# Ordenar y mostrar apellidos
apellidos.sort()
print("Apellidos ordenados:", apellidos)
# Caso 3: Agregar Nombres y Eliminar el Menos Extenso
nombres = []

while True:
    nuevo_nombre = input("Ingrese un nombre: ")
    nombres.append(nuevo_nombre)

    respuesta = input("¿Desea agregar otro nombre? (Sí/No): ")
    if respuesta.lower() == "no":
        break

nombre_menor_caracteres = min(nombres, key=len)
nombres.remove(nombre_menor_caracteres)

print(f"Lista de nombres sin el menos extenso: {nombres}")
