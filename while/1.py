num= int(input("Enter a number: ")) #Se le solicita al usuario qe digite un numero
result= 1 #Se crea una variable la cual almacena el resultado de la suma de los primeros numeros
start= 1 #Se crea una variable la cual cuenta del numero 1 hasta el numero ingresado

while start <= 10: #Se crea un ciclo el cual se ejecutara mientras el numero sea menor que 10
    if num > 10: #Se crea una condicion la cual actua o se ejecuta mientras que el numero que se ingreso sea mayor que el 10
        result *= start #Se multiplica el resultado acumulado por el valor actual que tiene el contador (inicio)
    else: #Si la condicion no se cumple se ejecutara lo siguiente
        result += start #En vez de multiplicar se suma el contador al resultado actual

        start += 1 #Incrementamos el valor del contador en 1
        if start > num: #Se cumple la condicion siempre y cuando se supera el numero ingresado
            break #Se sale del ciclo

if num > 10: #Si el numero es mayor que 10 se mostrara el siguiente mensaje:
    print(f"The multiplication of the first 10 numbers is: {result:.0f}")
else: #Si el numero no lo sipera el mensaje sera el siguiente
    print(f"The sum of the first 10 numbers is: {result:.0f}")
