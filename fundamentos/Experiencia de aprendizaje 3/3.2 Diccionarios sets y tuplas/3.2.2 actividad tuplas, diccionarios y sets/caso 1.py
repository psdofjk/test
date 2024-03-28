lista = []
for i in range(3):
  valor = input("Ingrese un numero: ")
  lista.insert(i, valor)
print(lista)

lista = []
for i in range(3):
  valor = input(f"Ingrese el {(i+1)}° nombre: ")
  lista.insert(i, valor)
print(lista)

longitudes = []
for i in lista:
    longitudes.append(len(i))
print(longitudes)

longitudmaslarga = max(len(i) for i in lista)

longitudmaslarga2= max(longitudes)

print(longitudmaslarga, longitudmaslarga2)

ubicacionmaslarga = []
for i, j in enumerate(lista):
   if len(j) == longitudmaslarga:
      ubicacionmaslarga.append(i)

print(ubicacionmaslarga)
#Aquí está desglosado lo que sucede en esta línea:

#  enumerate(lista): La función enumerate() toma una lista (en este caso lista) y devuelve una enumeración de los elementos de esa lista   junto con sus índices. Para cada elemento j en lista, enumerate() devuelve una tupla (i, j), donde i es el índice de j en la lista.

# for i, j in enumerate(lista): Esto es una iteración sobre la enumeración obtenida de lista. En cada iteración, i será el índice del     elemento y j será el elemento en sí.

# if len(j) == longitudmaslarga: Esto filtra los elementos j cuya longitud sea igual a longitudmaslarga.

# [i for i, j in enumerate(lista) if len(j) == longitudmaslarga]: Finalmente, esto crea una nueva lista que contiene los índices i de   los elementos que cumplen la condición anterior.

# Entonces, en resumen, esta línea de código genera una lista (ubicacionmaslarga) que contiene los índices de los elementos en la lista original (lista) que tienen la longitud más larga (longitudmaslarga).

