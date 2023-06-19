#Le pedimos al usuario que escriba la cantidad de temperaturas que desea colocar
n = int(input("Enter the number of temperatures to enter: "))

#Creamos un ciclo el cual validara que la cantidad de temperaturas es mayor que 0
while n <= 0:
    #Si la cantidad es menor aparecera el siguiente mensaje
    print("Error: You must enter a number greater than zero.")
    #Y se le pedira que ingrese la temperatura nuevamente
    n = int(input("Enter the number of temperatures to enter: "))

#Se crea una variable llamada tem_max con un valor llamado float('-inf) que sirve para que temp_max inicie con un valor extremadamente bajo asegurando que cualquier temperatura que ingrese el usuario sea mayor que ese valor facilitando la busqueda de la temperatura o el numero más alt@.
temp_max = float('-inf')

#En cambio en esta variable el valor que se le da es float('inf') Lo que hace es que temp_min comienza con un valor extremadamente alto asegurando que cualquier temperatura que ingrese el usuario sea mejor que la que se tiene por defecto haciendo mas facil el encontrar la temperatura o numero mas pequeño de todos o mas bajo
temp_min = float('inf')

#Se crea una variable la cual contara todos los datos ingresados por el usuario
counter = 0
#Se crea una variable la cual sumara todos los datos ingresado por el usuario en este caso la temperatura
sum_temp = 0

#Se crea un ciclo el cual nos permitira ingresar todas las temperaturas
while counter < n:
    #Le solicitamos al usuario que ingrese una temperatura
    temp = float(input(f"Enter the temperature {counter+1}: "))
    #Le sumamos la temperatura a la funcion sum_temp o suma_temperatura
    sum_temp += temp
    #Creamos unas condiciones las cuales identificaran la temperatura mas alta y la mas baja
    if temp >temp_max:
        temp_max = temp
    if temp < temp_min:
        temp_min = temp
    #Le incrememtamos al contador 1
    counter += 1
#Se crea una variable la cual calcula el promedio de las temperaturas
temp_ave= sum_temp / n

#Finalmente se mostrara todo el resultado
print(f"The highest temperature is {temp_max},the lowest temperature is {temp_min} and the average of all temperatures is {temp_ave}")
