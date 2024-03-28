nombre = []
apellido = []

for i in range(3):
    nombre.append(input(f"{i+1} nombre: "))
    apellido.append(input(f"{i+1} apellido: "))
    print(nombre[i] + " " + apellido[i])

nombreyapellido = []
for i in range(3):
    nombreyapellido.append(nombre[i] + " " + apellido[i])
print(nombreyapellido)