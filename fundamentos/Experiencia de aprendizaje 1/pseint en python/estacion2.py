# Algoritmo Estacion_Servicio

# Definir variables
nivel_bencina = 0.0
litros_bencina = 0.0
tipo_bencina = 0

# Mensajes de bienvenida e ingreso de datos
print("Bienvenido a la Bencinera")
litros_bencina = float(input("Por favor, indique cuántos litros de bencina tiene su auto:"))

# Asignar el nivel de bencina
nivel_bencina = litros_bencina

# Verificar el nivel de bencina y sugerir recarga si es necesario
if nivel_bencina < 10:
    print("Su nivel de bencina es bajo. Se sugiere cargar más.")
    
    # Solicitar el tipo de bencina
    print("Seleccione el tipo de bencina:")
    print("1. 93 litros")
    print("2. 95 litros")
    print("3. 97 litros")
    
    tipo_bencina = int(input())
    
    # Según el tipo de bencina, mostrar mensaje correspondiente
    if tipo_bencina == 1:
        print("Ha elegido 93 lts regular. Se está cargando regular.")
    elif tipo_bencina == 2:
        print("Ha elegido 95 lts plus. Se está cargando plus.")
    elif tipo_bencina == 3:
        print("Ha elegido 97 lts premium. Se está cargando premium.")
    else:
        print("Opción no válida. Operación cancelada.")
else:
    print("Su nivel de bencina es adecuado. No es necesario cargar más.")

# Mensaje de agradecimiento
print("Gracias por venir a la bencinera.")
