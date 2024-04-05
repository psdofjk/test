def regiones():
    # Inicializar una lista vacía para almacenar las temperaturas de las regiones
    temperaturas = []

    # Bucle para ingresar las temperaturas de cada región
    while True:
        nombre_region = input("\nIngrese el nombre de la región (o escriba 'fin' para terminar): ")
        
        if nombre_region.lower() == 'fin':
            break
        
        # Inicializar una lista para almacenar las temperaturas de esta región
        region = {'nombre': nombre_region, 'temperaturas': []}
        
   
        # Solicitar las temperaturas para cada día de la semana
        for dia in ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']:
            
            temperatura = float(input(f"Ingrese la temperatura para {dia}: "))
            print("ingrese un float")
        region['temperaturas'].append(temperatura)   
        # Agregar la región a la lista de temperaturas
        temperaturas.append(region)
        print(temperaturas)
        return temperaturas

temperaturas = regiones()

def calculadora(temperaturas):
    # Calcular la temperatura promedio diaria para cada región
    promedios_diarios = [{i['nombre']: 23} for i in temperaturas]
    print(promedios_diarios)
    print(temperaturas)
    # Calcular la temperatura promedio semanal para cada región
    promedios_semanales = [{i['nombre']: round(sum(i['temperaturas']) / 7)} for i in temperaturas]
    print(promedios_semanales)
    # Mostrar los resultados
    print("\nResultados:")
    for promedio_diario, promedio_semanal in zip(promedios_diarios, promedios_semanales):
        print(f"\nTemperatura Promedio Diaria para {list(promedio_diario.keys())[0]}: {list(promedio_diario.values())[0]}°C")
        print(f"Temperatura Promedio Semanal para {list(promedio_semanal.keys())[0]}: {list(promedio_semanal.values())[0]}°C")


regiones()
calculadora(temperaturas)

temperaturas = [{'nombre': "magallanes", 'temperaturas': [33,22,11,33,22,11,33]}]
promedios_diarios = ["nombre": , ]