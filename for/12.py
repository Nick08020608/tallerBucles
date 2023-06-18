estudiantes = int(input("Ingresa el numero de estudiantes: "))

nota_alta = 0 #Se le da valor a  nota_alta
nota_baja = float('inf') #Se utiliza el float('inf) para que el valor nuca se actualice ya que cualquier nota sera mayor que este valor
total_notas = 0 #se le da valor a total_notas

for i in range(estudiantes): #Se crea un ciclo con la restriccion que coloca el maestro
    nota= float(input(f"Ingresa una nota del estudiante {i+1}: "))
    total_notas +=nota #Se saca el total de las notas

    if nota > nota_alta: #Se crea una condicion la cual nos permite sacar la nota mas alta
        nota_alta = nota
    if nota <= nota_baja: #Se crea una condicion que nos permite sacar la nota mas baja
        nota_baja = nota

promedio = total_notas / estudiantes #Sacamos el promedio de las notas

print(f"La nota mas alta de los estuantes es {nota_alta}, la nota mas baja seria {nota_baja} y el promedio de notas del estudiante seria {promedio}.") #Finalmente imprimimos todos los datos :)