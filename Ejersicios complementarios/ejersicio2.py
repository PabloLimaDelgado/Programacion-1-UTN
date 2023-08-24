arreglo_dia = input("Ingrese la fecha actual en formato “día,DD/MM”: ")

arreglo_dia_semana = (arreglo_dia.split(',')[0]).lower()
dia_de_semana_num = int((arreglo_dia.split(',')[1]).split('/')[0])
mes_num = int((arreglo_dia.split(',')[1]).split('/')[1])

if((arreglo_dia_semana == "lunes" or arreglo_dia_semana == "martes" or arreglo_dia_semana == "miercoles"
   or arreglo_dia_semana == "jueves" or arreglo_dia_semana == "viernes") and 
   (dia_de_semana_num >= 0 and dia_de_semana_num <= 31) and (mes_num >= 0 and mes_num <= 12)):
    
    if(arreglo_dia_semana == "lunes" or arreglo_dia_semana == "martes" or arreglo_dia_semana == "miercoles"):

        examen = input("Hubo examen “si/no”: ")
        examen = examen.lower()

        if(examen == "si"):
            examen_aprobados = int(input("Ingrese el número de alumnos aprobados: "))
            examen_desaprobados = int(input("Ingrese el número de alumnos desaprobados: "))
            porcentaje_aprobados = 100 * examen_aprobados / (examen_aprobados + examen_desaprobados)

            print(f"El porcentaje de alumnos aprobados es: {porcentaje_aprobados}%") 

        elif(examen == "no"):
            print("Ese dia no hubo examen")

        else:
            print("Se produjo un error")

    elif(arreglo_dia_semana == "jueves"):
        porcentaje_asistencia = int(input("Ingrese el porcentaje de asistencia: "))
        if(porcentaje_asistencia > 50):
            print("Asistio la mayoria")
        else:
            print("No asistio la mayoria")

    elif(arreglo_dia_semana == "viernes"):
        if((dia_de_semana_num == 1 and mes_num == 1) or mes_num == 7):
            print("Comienzo del nuevo ciclo")
            cant_alumnos_nuevos = int(input("Cantidad de alumnos del nuevo ciclo: "))
            arancel_por_alumno = int(input("Ingrese el arancel por alumno: "))
            print(f"El ingreso total es de {cant_alumnos_nuevos*arancel_por_alumno}$")
else:
    print("Se produjo un error")
    