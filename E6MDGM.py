#Ejercicio 6
#MDGM

encendido = input('¿La computadora enciende? (si/no): ')
pitido = input('¿Escuchas algun pitido al encender? (si/no): ')
imagen = input('¿El monitor muestra imagen? (si/no): ')

if encendido == "no":
    print('Diagnostico: Verificar conexión electrica o fuente de poder')
else:
    if pitido == "si":
        print('Diagnostico: Problema de hardware detectado (memoria RAM, tarjeta madre).')
    else:
        if imagen == "no":
            print('Diagnostico: Revisar conexion del monitor o tarjeta de video')
        else:
            print('Diagnostico: La computadora parece encender correctamente')

            