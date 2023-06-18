num= int(input("Enter a number: "))
#se crea 2 variables cuyo valor sea 0 contador sirve para contar los numeros desde el 1 hasta el numero que digito el usuario
counter= 0
result= 0

#Se crea un ciclo el cual se repetira mientras el contador sea menor que el numero ingresado
while counter <= num:
    #Se crea una condicional la cual identificara cuando un numero sea par
    if counter% 2 ==0:
        #Se suma el contador al resultado
        result += counter
    #Se incrementa de ah 1 el contador
    counter += 1

#Mostramos lo que queremos en la pantalla
print(f"The sum of the even numbers from 0 to {num} is: {result}.")
