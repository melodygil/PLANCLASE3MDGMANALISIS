#Ejercicio 10
#MDGM
nombre= input('Introduce tu nombre: ')
proyectos = int(input('¿Cuantos proyectos completaste este año?'))
cursos = int(input('¿CUantos cursos de formacion completaste este año?'))
reconocimiento = input('¿Recibiste un reconocimiento oficial? (si/no): ').lower()

if proyectos >= 5 and cursos >=3 and reconocimiento == 'si':
    print(nombre, ' ¡Felicidades! Eres elegible para el bono maximo.')
elif proyectos >= 3 and cursos >=2:
    print(nombre, ' Eres elegible para un bono estandar.')
elif proyectos >=1:
    print(nombre, ' Recibiras un bono de participacion.')
else:
    print(nombre, ' No calificas para un bono este año. ¡Animo para la proxima!')
