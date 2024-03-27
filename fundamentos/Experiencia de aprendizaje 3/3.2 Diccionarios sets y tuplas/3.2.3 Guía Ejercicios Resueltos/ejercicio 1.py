frecuencia = {}

textoarevisar = input("Porfavor ingrese su texto: ")
textospliteado = textoarevisar.split()

for i in textospliteado:
    frecuencia[i] = frecuencia.get(i, 0) + 1

for i, j in frecuencia.items():
    print(f"{i}:{j}")
