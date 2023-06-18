#Definimos una funcion
def calculate_average():
    #Le pedimos al maestro que ingrese la cantidad de notas que hay
    quantity_notes= int(input("Enter the numbers of notes: "))
    #Creamos una variable suma para acumular la suma de todas las notas
    sum = 0
    #Creamos una variable la cual cuenta el numero de notas que se ingresaran
    counter = 0
    #Se crea un ciclo el cual le solicitara al usuario que ingrese la cantidad de notas ya propuestas
    while counter < quantity_notes:
        #Se le pide que ingrese la nota
        note= float(input(f"Enter the note {counter+1}: "))
        #Se realiza la suma de la varible
        sum += note
        #Se incrementa en 1 para que pueda pasar a la siguiente nota
        counter += 1
    #Se calcula el promedio de las notas
    average = sum/quantity_notes
    #Devolvemos el valor del promedio
    return average
#Se llama a la funcion de calculo de promedio (calculate_average)
average_end = calculate_average()
#Mostramos el promedio calculado
print(f"The student average is: {average_end}")