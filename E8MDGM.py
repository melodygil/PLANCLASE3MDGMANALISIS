#Ejercicio 8
#MDGM

contraseña = input('Introduce una contraseña para evaluacion: ')

longitud = len(contraseña)
contiene_numeros = any(char.isdigit() for char in contraseña)
contiene_mayusculas = any(char.isdigit() for char in contraseña)

if longitud >= 12 and contiene_numeros and contiene_mayusculas:
    print('Contraseña fuerte')
elif longitud >= 8:
    print(' Contraseña moderada. Recomemdo mejor')
else:
    print('¿Longitud de la contraseña? ', longitud)
    print('¿Contiene numeros?: ',contiene_numeros)
    print('¿Contiene tiene mayusculas?', contiene_mayusculas)
