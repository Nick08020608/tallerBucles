#Se le solicita la usuario que porfavor digite un numero
n = int(input("Enter a number: "))
#Se crea una variable la cual va a almacenar la suma de todos los numero impares que existan 
sum_odd= 0
#Se crea otra variable la cual va a contar todos los numeros impares que existan
counter_odd = 0
#Se crea una nueva variable la cual se va a encargar de iniciar el conteo desde 1 y no desde 0
number_current = 1
#Se crea un ciclo el cual se ejecutara siempre y cuando el numero sea menor que el numero ingresado por el usuaario
while number_current <= n:
    #Se crea una condicion la cual verificara si el numero actual o number_current es impar
    if number_current % 2 != 0:
        #Suma todos los numeros impares que existan
        sum_odd += number_current
        #El contador se incrementa
        counter_odd += 1
    #Se avanza al proximo numero (pues se le suma 1 al contador actual para que siga realizandose el ciclo hasta finalizar)
    number_current += 1
#Se imprime el resultado
print(f"The sum of numbers odd is: {sum_odd}\nThe quantity of numbers odd is: {counter_odd}")