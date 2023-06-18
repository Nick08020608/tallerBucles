n= int(input("¿Que tabla quieres ver? Digita un numero del 0 al 10: ")) #Le pedimos al usuario que dijite la tabla que desea ver
print(f"--Tabla del {n}--")
for i in range (11): #Le colocamos el rango que deseamos tener es decir hasta que numero queramos ver en la tabla
    mul = i * n #Se multiplica el numero por el rango o la iteracion
    print(f"{n}x{i}={mul}") #Mostramos la tabla completa UwU
