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
