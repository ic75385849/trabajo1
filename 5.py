import calendar

def obtener_dia_semana(dia, mes, anio):

    dia_semana = calendar.weekday(anio, mes, dia)
    

    nombre_dia = calendar.day_name[dia_semana]
    
    return nombre_dia

def main():

    dia_nacimiento = int(input("Ingresa el día de tu nacimiento: "))
    mes_nacimiento = int(input("Ingresa el mes de tu nacimiento (número): "))
    anio_nacimiento = int(input("Ingresa el año de tu nacimiento: "))
    
    dia_semana_nacimiento = obtener_dia_semana(dia_nacimiento, mes_nacimiento, anio_nacimiento)

    print(f"Tu fecha de nacimiento ({dia_nacimiento}/{mes_nacimiento}/{anio_nacimiento}) fue un {dia_semana_nacimiento}.")

if __name__ == "__main__":
    main()
