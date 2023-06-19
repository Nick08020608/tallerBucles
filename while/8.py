#Se le pide al usuario que escriba un numero entero
number = int(input("Enter an integer greater than zero: "))
#Se crea un ciclo el cual se ejecutara siempre y cuando sea menor o igual a cero
while number <= 0:
    #Si pasa esto se mostrara un error
    print("Error: You must enter a number greater than zero. ")
    #Se le pide al usuario que dijite otro numero
    number= int=input("Enter an integer greater than zero: ")
#Se manda un mensaje en el cual le informa al usuario los divisores del numero
print(f"Los divisores del número {number} are: ")
#Se crea una variable la cual inicia el divisor en 1
divider = 1
#Se crea un nuevo ciclo el cual solo se ejecutara cuando el numero sea menor o igual que el numero ingresado por el usuario
while divider <= number:
    #Se crea una condicion la cual nos permite identificar si el numero es divisible por el divisor actual
    if number % divider == 0:
        #Si es divisible se mostrara en la pantalla
        print(divider)
    #Se crea una variable la cual incrementa el valor de el divisor una vez antes de continuar
    divider += 1
