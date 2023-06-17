numero = int(input("Ingrese un número: "))

if numero > 10:
    resultado = 1
    for i in range(1, 11):
        resultado *= i
else:
    resultado = 0
    for i in range(1, 11):
        resultado += i

resultado *= 3

print("El resultado es:", resultado)

