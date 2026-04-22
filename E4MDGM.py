#Ejercicio 4
#MDGM

estatura = float(input('Introduce tu estatura en metros: '))

if estatura >= 1.30:
    print('Puedes subir solo a la montaña Rusa.')
elif estatura >=1.20:
    print('Puedes subir con un acompañante adulto.')
else:
    print('No puedes subir a la montaña rusa.')