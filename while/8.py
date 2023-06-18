#Se le pide al usuario que escriba un numero entero
number = int(input("Enter an integer greater than zero: "))
#Se crea un ciclo el cual se ejecutara siempre y cuando sea menor o igual a cero
while number <= 0:
    #Si pasa esto se mostrara un error
    print("Error: You must enter a number greater than zero. ")
    number= int=input("Enter an integer greater than zero: ")
print(f"Los divisores del número {number} are: ")
divider = 1
while divider <= number:
    if number % divider == 0:
        print(divider)
    divider += 1
