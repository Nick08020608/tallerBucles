num= int(input("Ingresa un numero: ")) #Le pedimos al usuario que dijite un numero

def operacion (num): #Definimos una funcion
    if num > 10:#Creamos una condicion
        mul = 1
        for i in range(1,num+1):#Le colocamos un rango a dicha funcion
            mul *=i #multiplicamos la funcion por la itentacion
        return mul #Retornamos a la funcion
    else:
        sum = 0 #Le damos un valor a sum
        for i in range (1,num+1): #Le colocamos un rango a dicha funcion
            sum +=i #sumamos la funcion a la itentacion
        return sum
resultado= operacion(num) #Realizamos el resultado final
print(f"La multiplicacion de {num} es {resultado}.") #Y colocamos el resultado final