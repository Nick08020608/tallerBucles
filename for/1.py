cantidadNumero=int(input("Ingrese el numero de elementos que quiere sumar: ")) #Le pedimos al usuario la cantidad de veces que queremos que repita el numero
sum=0 #Le damos un valor a la variable suma

for i in range(cantidadNumero): #Creamos un ciclo al cual le colocamos el rango que quiso el usuario (linea 3)
    num=int(input("Ingrese un numero: ")) #Le pedimos que escriba el numero
    sum += num

print(f"la suma de los {cantidadNumero} numeros es {sum}") #finalmente suma los numeros que propuso el usuario :)

