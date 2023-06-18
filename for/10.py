numero=int(input("Ingresa un numero: "))
def program(num): #Definimos una funcion.
    if num > 10: #Creamos unas condicionales
        divisores = [] #Creamos una lista vacia para que almacene los datos
        for i in range(1,num+1): #Creamos un ciclo el cual pocea el rango que el usuario coloque
            if  num % i == 0: #Creamos una condicion la cual nos permita identificar si un numero es par o impar
                divisores.append(i) #Aqui colocamos la cantidad de items que tendra una tabla
        return divisores #Finalmente retornamos toda la tabla
    else:
        print(f"lo siento el numero {num} es menor o igual que 10") #Esto sera lo que aparecera si no se cumple dicha conficion en el ciclo
resultado= program(numero)
print(f"los divisores de {numero} son: {resultado}")
