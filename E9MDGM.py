#Ejercicio 9
#MDGM
area = input('¿En que area es el problema?(software/hardware/red): ')
gravedad = input('¿Que tan grave es el problema (alta/media/baja)')

if area == "software" and gravedad == "alta":
    print('Ticket: Prioridad critica. Escalar a desarrolladores senior. ')
elif area == "software" and gravedad == "media":
    print('Ticket: Prioridad alta. REsolver en menos de 24 horas.')
elif area == "hardware" and gravedad == "alta":
    print('Ticket: Prioridad critica.Enviar equipo de reparacion')
elif area == "hardware" and gravedad == "media":
    print('Ticket: Prioridad alta. Evaluacion remote')
elif area == "red" and gravedad == "alta":
    print('Ticket: Prioridad critica: Escalar a administradores de red.')
elif area == "red" and gravedad == "media":
    print('Ticket: Prioridad alta. Diagnostico inmediato.')
else:
    print('Ticket: Prioridad normal. Programar revision en 48 horas')