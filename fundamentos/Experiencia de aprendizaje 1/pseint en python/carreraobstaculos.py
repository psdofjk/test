# Algoritmo Carrera_obstaculos

# Paso 1: Inicio de la carrera
print("¡Comienza la carrera!")

# Paso 2: Primer obstáculo
print("1. Primer obstáculo: Valla.")
respuestavalla = input("¿Encuentras una valla en el camino? (si/no): ")

if respuestavalla.lower() == "si":
    print("Debes saltar la valla.")
else:
    print("Bien hecho. Continua corriendo.")

# Paso 3: Segundo obstáculo
print("2. Segundo obstáculo: Túnel.")
respuestatunel = input("¿Encuentras un túnel en el camino? (si/no): ")

if respuestatunel.lower() == "si":
    print("Debes cruzar el túnel.")
else:
    print("Muy bien. Debes seguir corriendo.")

# Paso 4: Tercer obstáculo
print("3. Tercer obstáculo: Laguna.")
respuestalaguna = input("¿Ves una laguna en el camino? (si/no): ")

if respuestalaguna.lower() == "si":
    print("¡Cuidado!. Debes nadar, te agotas y devuelves. Pierdes la carrera.")
else:
    print("¡Felicidades! Has llegado a la meta.")

# Paso 5: Fin de la carrera
print("Fin de la carrera.")
