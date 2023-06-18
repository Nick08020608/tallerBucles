numero_notas = int(input("Ingrese la cantidad de notas a capturar: ")) #Se le pide al maestro escribir la cantidad de notas que hay.
suma = 0 #Se le da un valor a la variable suma para luego sumarsela a las notas

for i in range(numero_notas): #Creamos un ciclo con un rango e cual es el que coloca el usuario o maestro
    nota = float(input("Ingrese la nota {}: ".format(i+1))) #En este caso utilizamos el format para poder mostrar el numero de notas que se colocan.
    suma += nota #Se suman todas las notas

promedio = suma / numero_notas #Finalmente se saca el promedio de notas dividiendo la suma de todas las notas sobre el numero de notas.

print(f"El promedio del estudiante es: {promedio:.1f}")
