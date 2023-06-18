num= int(input("Ingresa un numero: ")) #Pedimos el ingreso de un numero
num1=int(input("Ingresa otro numero: ")) #Pedimos el ingreso de un numero
def programa(num,num1): #Definimos una funcion
    if num > num1:#Creamos una condicional
        sum = 0
        for i in range(1,num1+1):#Creamos un ciclo dentro de la condicion
            sum += i
        return sum
    elif num == num1: #Creamos otra condicion por si no se cumple la anterior
        print(f"los numeros {num} y {num1} son iguales.")
    else: #Creamos otra por si no se cumple ninguna
        print(f"el numero {num1} es mas grande que {num}")
resultado= programa(num, num1) #Sacamos el resultado :)
print(resultado) #Imprimimos todo :)
