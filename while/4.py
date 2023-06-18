#Pedimos al usuario que digite 2 numeros
num=int(input("Enter the first number: "))
num1=int(input("Enter the second number: "))
#Creamos dos variables las cuales son contador(counter) y contar numeros (count_numbers) y le damos un valor a cada uno
counter = num
count_numbers = 0

while counter <= num1: #Creamos una condicion la cual nos permita identificar si el primer numeros (num) es mayor que el segundo (num1)
    if num >= num1:
        print("The first number is minor that the second number.")
        break
    counter += 1
    count_numbers += 1
#Creamos otra condicional en donde nos dice si el primer numero es menor que el numero 2 entoces se realizara el comentario que queremos que aparesca
if num < num1:
    print(f"The count of the numbers between {num} and {num1} is {count_numbers}.")
