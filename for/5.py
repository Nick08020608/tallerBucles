numero= int(input("Digita un numero: "))#Le pedimos al usuario que dijite un numero
suma_impares = 0 #Le damos un valor a la variable suma_impares 
cantidad_impares = 0 #Le damos un valor a la variable cantidad_impares


for i in range(numero + 1): #creamos un ciclo en donde se le sume 1 al rango numero
    if i % 2 !=0: #Creamos una condicional la cual 
        suma_impares += i #Se suman la cantidad de numero impares que hay
        cantidad_impares += 1 #Cuenta la cantidad de numeros impares que hay

print(f"La suma de los numeros impares es: {suma_impares}.") #Se muestra la suma de todos los numeros impares.
print(f"La cantidad de numeros impares que hay es: {cantidad_impares}.") #Se muestra la cantidad de numeros impares que hay en la funcion.
