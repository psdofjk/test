# Ejercicio 1: Frecuencia de Palabras en un Texto
texto = input("Ingrese un texto: ")
palabras = texto.split()

frecuencia_palabras = {}
for palabra in palabras:
    palabra = palabra.lower()  # Convertir a minúsculas para evitar distinción por mayúsculas
    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1

print("Frecuencia de palabras:")
for palabra, frecuencia in frecuencia_palabras.items():
    print(f"{palabra}: {frecuencia}")


# Ejercicio 2: Conjunto de Números Primos
rango_inferior = int(input("Ingrese el rango inferior: "))
rango_superior = int(input("Ingrese el rango superior: "))

numeros_primos = {num for num in range(rango_inferior, rango_superior + 1) if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))}

print("Conjunto de números primos:", numeros_primos)



# Ejercicio 3: Tuplas y Conjuntos en Combinación
datos_personales = []

while True:
    nombre = input("Ingrese un nombre: ")
    if nombre.lower() == "fin":
        break
    edad = int(input("Ingrese la edad: "))
    datos_personales.append((nombre, edad))

edades_unicas = {edad for _, edad in datos_personales}

print("Edades únicas presentes:", edades_unicas)

