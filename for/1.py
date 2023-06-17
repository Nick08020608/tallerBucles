#sumar los primeros numeros, solicite al usuario el numero de elementos a sumar.

cantidadNumero=int(input("Ingrese el numero de elementos que quiere sumar: "))
sum=0

for i in range(cantidadNumero):
    num=int(input("Ingrese un numero: "))
    sum += num

print(f"la suma de los {cantidadNumero} numeros es {sum}")

