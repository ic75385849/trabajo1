import datetime

fecha_nacimiento= input("ingresa tu fecha de nacimiento (AAA-MM-DD): ")
fecha= datetime.datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
dias_semana= ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
dia_semana= dias_semana[fecha.weekday()]
print(f"nacistes un {dia_semana}.")
    