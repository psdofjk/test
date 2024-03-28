# Prestamo banco

print("Bienvenido al banco La gallina de los huevos dorados.");
print("Ingresa nombre del cliente: ");
nombre_cliente = str(input());
print("Ingresa RUT cliente. (sin guion y puntos): ");
rut_cliente = int(input());
print("Ingresa monto solicitado: ");
monto_solicitado = int(input());
print("Ingrese cantidad de cuotas: ");
cantidad_cuotas = int(input());

interes = (monto_solicitado * cantidad_cuotas / 100);
valor_total = (monto_solicitado + interes);
valor_cuota = (valor_total / cantidad_cuotas);

print("Banco La gallina de los huevos de oro.");
print("Nombre cliente: ", nombre_cliente), ("RUT: ", rut_cliente);
print ("Monto solicitado: $", monto_solicitado); 
print("Cantidad de cuotas: ", cantidad_cuotas);
print("Interes: $ ", interes);
print("Valor cuota: $ ", valor_cuota);

print("Gracias por confiar en nuestro banco.");




