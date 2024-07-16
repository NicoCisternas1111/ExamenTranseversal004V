"""
trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
La aplicación deberá poseer un menú con las siguientes funcionalidades:
1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadísticas.
4. Reporte de sueldos
5. Salir del programa
Cada función se detalla a continuación:
1. Asignar sueldos aleatorios
Para la generación de estos sueldos debe crear una función capaz de generar los 10 sueldos de forma aleatoria los que serán usados posteriormente para la ejecución del programa.
2. Clasificar sueldos
Deberá desarrollar una función que permita mostrar la lista de empleados con su sueldo y su respectiva clasificación según el siguiente esquema
3. Ver estadísticas
Crear una función que permita mostrar por pantalla los siguientes datos con respecto a los sueldos:
 Sueldo más alto
 Sueldo más bajo
 Promedio de sueldos
 Media geométrica
4. Reporte de sueldos
La aplicación deberá poseer una función para mostrar el detalle de los sueldos de los trabajadores, según la siguiente regla de negocio:
 Descuento salud 7%
 Descuento AFP 12%
 Sueldo líquido calculado en base al sueldo base menos el descuento en salud y menos el descuento afp.
Estos datos se deberán exportar a un archivo de texto separado por comas (.csv) para su posterior lectura en otra aplicación.
"""

import random
import csv
import math
import time


trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
sueldos = []

def sueldos_aleatorios():
    global sueldos
    for i in range(10):
        sueldos.append(random.randint(300000,2500000))
    print ("Sueldos asignados aleatoriamente")
        
def class_sueldos():
    print("Sueldos menores a $800.000 TOTAL:", len([x for x in sueldos if x < 800000]))
    if len([x for x in sueldos if x < 800000]) > 0:
        print("""
Nombre empleado                    Sueldo""")
        for t,s  in zip(trabajadores, sueldos):
            if s < 800000:
                print(f"""
{t}                    ${s}\n""")
    
    print("\nSueldos entre $800.000 y $2.000.000 TOTAL:", len([x for x in sueldos if 800000 <= x <= 2000000])) 
    if len([x for x in sueldos if 800000 <= x <= 2000000]) > 0:
        print("""
Nombre empleado                    Sueldo""")
        for t, s in zip(trabajadores, sueldos):
            if 800000 <= s <= 2000000:
                print(f"""
{t}                    ${s}\n""")
    
    print("\nSueldos superiores a $2.000.000 TOTAL:", len([x for x in sueldos if x > 2000000]))
    if len([x for x in sueldos if x > 2000000]) > 0:
        print("""
Nombre empleado                    Sueldo""")
        for t, s in zip(trabajadores, sueldos):
            if s > 2000000:
                print(f"""
{t}                   ${s}\n""")
    
    print("\nTOTAL SUELDOS:", sum(sueldos))
            
def stats_sueldos():
    mas_bajo = min(sueldos)
    mas_alto = max(sueldos)
    prom = sum(sueldos)/len(sueldos)
    medgem = math.exp(sum([math.log(s) for s in sueldos])/len(sueldos))
    print(f"""
Sueldo mas bajo: ${mas_bajo}
Sueldo mas alto: ${mas_alto}
Promedio de sueldos: ${prom}
Media Geometrica: ${medgem}""")
    
def reporte_sueldos():
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for trabajador, sueldo in zip(trabajadores, sueldos):
            des_salud = sueldo * 0.07
            des_afp = sueldo * 0.12
            liquid = sueldo - des_salud - des_afp
            writer.writerow([trabajador, sueldo, des_salud, des_afp, liquid])
            print (f"Nombre empleado: {trabajador}\nSueldo base: ${sueldo}\nDescuento Salud: ${des_salud}\nDescuento AFP: ${des_afp}\nSueldo liquido: ${liquid}")
            
def salir():
    print("Finalizando programa...")
    print("Desarrollado por Nicolas Cisternas")
    print("RUT 19.818.561-2")
    time.sleep(5)
    
def menu():
    while True:
        op = input ("Por favor selecciona una de las siguientes opciones:\n1.- Asignar sueldos aleatorios\n2.- Clasificar sueldos\n3.- Ver estadisticas\n4.- Reporte de sueldos\n5.- Salir del programa\n")
        
        if op == "1":
            sueldos_aleatorios()
        elif op == "2":
            class_sueldos()
        elif op == "3":
            stats_sueldos()
        elif op == "4":
            reporte_sueldos()
        elif op == "5":
            salir()
        else:
            print("Por favor ingresa una opción valida")
            continue
        
if __name__ == "__main__":
    menu() 