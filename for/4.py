numero = int(input("Ingrese un número: ")) #Se le pide un numero al usuario
suma = 0 #Se le da un valor a la variable suma

for i in range(0, numero): #Se le coloca un rango al bucle en este caso el que coloca el usuario
    if i % 2 == 0: #Se coloca solo para que lea numero impares
        suma += i #Finalmente se le suma todos los impares que hay en el programa
print(f"La suma del 0 hasta el numero propuesto por el usuario es: {suma}") #finalmente colocamos el mensaje final :)
