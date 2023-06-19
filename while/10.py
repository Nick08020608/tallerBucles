#Se le pide al usuario que escriba la cantidad de estudiantes que hay
n = int(input("Enter the number of students: "))
#Se crea una variable en la cual se almacenara la nota mas alta
note_max = float('-inf')
#Se crea una variable en la cual se almacena la nota mas baja
note_min = float('inf')
#Se crea una variable la cual almacenara la suma de todas las notas
sum_note = 0
#Se crea una variable la cual cuente la cantidad de estudiantes
counter = 0
#Creamos un ciclo el cual pide el ingreso de todas las notas
while counter < n:
    print(f"Enter the 3 student grades {counter+1}: ")
    #Se crea otro ciclo el cual evitara futuros problemas al ingresar la primera nota
    while True:
        try:
            #Se le solicita al usuario que escriba o digite la primera nota
            note = float(input("Enter the first note: "))
            #Salimos del ciclo si la nota es un numero invalido
            break
        except ValueError:
            #Si el numero es invalido se procede a mostrar este mensaje
            print("Enter a number valid...")
    #Se crea otro ciclo el cual evitara futuros problemas al ingresar la segunda nota
    while True:
        try:
            #Se le solicita al usuario que escriba o digite la segunda nota
            note1 = float(input("Enter a second note: "))
            #Salimos del ciclo si la nota es un numero invalido
            break
        except ValueError:
            #Si el numero es invalido se procede a mostrar este mensaje
            print("Enter a number valid...")
    #Se crea otro ciclo el cual evitara futuros problemas al ingresar la tercera parte
    while True:
        try:
            #Se le solicita al usuario que escriba o digite la tercera nota
            note2 = float(input("Enter a third note: "))
            #Salimos del ciclo si la nota es un numero invalido
            break
        except ValueError:
            #Si el numero es invalido se procede a mostrar este mensaje
            print("Enter a number valid...")

    #Se verifica si las notas que se ingresaron son mas altas o bajas
    note_max = max(note_max,note,note1,note2)
    note_min = min(note_min,note,note1,note2)
    #Se crea una variable la cual suma todas las notas
    sum_note = sum_note + note + note1 + note2
    #Se Incrementa en 1 al contador
    counter += 1
#Se calcula el promedio de las notas dividiendo la suma total de las notas por el total de notas
note_total = n * 3
average = sum_note / note_total
#Mostramos el resultado
print(f"the highest note is: {note_max}.\nthe lowest note is: {note_min}.\nThe grade point average is: {average:.1f}.")