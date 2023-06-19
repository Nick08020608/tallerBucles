#Se le pide al usuario que ingrese el monto total de las facturas y que porfavor finalice con un cero para que pueda finalizar como el registro de dicho monto
amount = float(input("Enter the amount of the bills (Enter 0 to finish): "))
#Se crea una variable que almacenará el total de factoras (total_bills)
total_bills = 0
#Se crear un ciclo el cual se podra ejecutar siempre y cuando el monto que se ingrese no sea 0
while amount != 0:
    #Se suma el monto total de las facturas
    total_bills += amount
    #Se le pide al usuario que ingrese el monto de la proxima factura
    amount = float(input("Enter the amount of the bills (Enter 0 to finish): "))
#Se crea una condicional la cual verificará si el total de facturas supero los $1000
if total_bills > 1000:
    #Si se cumple la condicion se le realizará un descuento al usuario del 10%
    discound = total_bills * 0.1
    #Se se crea otra variable la cual calculará el total a pagar
    total_pay = total_bills - discound
else:
    #Si no se cumple la funcion simplemente el total a pagar será el total de todas las facturas
    total_pay = total_bills
#Mostramos el resultado en la pantalla
print(f"The total to pay is: {total_pay}")