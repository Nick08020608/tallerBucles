#Se define la variable calculate_sum
def calculate_sum():
    num = []
    #Se crea un ciclo en el cual se le pide al ingresar un numero entero
    while True:
        #Se utiliza un bloque try-except para capturar un posible error al intentar convertir la entrada del usuario a un numero entero.
        try:
            #Se le pide al usuario que dijite un numero
            number = int(input("Please enter a whole number (0 to end): "))
            #Se crea una condicional en la cual si se ingresa un numero 0 se acaba el ciclo
            if number == 0:
                break
            #Se agrega un numero a la lista de "num"
            num.append(number)
        #En el caso de que exista un error se muestra un mensaje en el cual se le solicita que escriba un nuevo numero
        except ValueError:
            print("Error: You must enter a valid integer.")
    #Se calcula la sumatoria de los numeros utilizados en la funcion sum() y lo asigna a la variable "sumatoria"
    summation = sum(number)
    #Se devulve la sumatoria calculada
    return summation
#Llama a la funcion "calculate_sum()"
final_sum = calculate_sum()
#para obtener la sumatoria
print(f"The sum of the entered numbers is: {final_sum}")
