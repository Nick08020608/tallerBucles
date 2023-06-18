numero= int(input("Ingresa un numero: ")) #Le pedimos al usuario que dijite un numero

if numero <= 0: #Creamos una condicional para los numero que no cumplan la funcion
    print("Numero inválido. Por favor ingrese un numero que sea mayor a cero: ")
else:
    print(f"Los divisores de {numero} son: ") #Cuando se cumple la funcion se cumple el ciclo

for i in range(1, numero + 1): #Finalmente realizamos el ciclo.
    if numero % i == 0:
        print(i)
