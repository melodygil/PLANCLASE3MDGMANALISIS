#Ejercicio 7
#MDGM
anios_experiencia = int(input('Introduce tus años de experiencia en programacion: '))
tecnologia = input('¿Prefieres trabajar en (backend/frontend/fullstack)?')

if anios_experiencia >=5:
    senior= True
else:
    senior = False

if tecnologia == "backend" and senior:
    print('Proyecto asignado: Microservicios para banca digital.')
elif tecnologia == "frontend" and senior:
    print('Proyecto asignado: Plataforma de ventas en tiempo real.')
elif tecnologia == "fullstack" and senior:
    print('Proyecto asignado: Sistema ERP completo. ')
elif tecnologia == "backend" and not senior:
    print('Proyecto asignado: APIs basicas para e-commerce.')
elif tecnologia == "frontend" and not senior:
    print('Proyecto asignado: Diseño de landing pages.')
elif tecnologia == "fullstack" and not senior:
    print('Proyecto asignado: Modulo de autenticacion de usuarios. ')
else:
    print('Error: tecnologia ingresada no reconocida')

