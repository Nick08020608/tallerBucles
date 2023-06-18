temp_cant=int(input("¿Cuantas temperaturas se van a introducir?: "))
#Se le da valor a las variables temp_alta,temp_baja,temp_total:
temp_alta= 0
temp_baja= float('inf')
temp_total= 0

for i in range(temp_cant): #Creamos un ciclo cuyo rango es temp_cant
    temp= int(input(f"Ingresa la temperatura {i+1}: ")) #Se le pregunta al usuario las temperaturas
    temp_total += temp #Se calcula el total de todas las temperaturas
    #Se crea unas condiciones las cuales calcularan la temperatura mas alta y baja que escribio o dijito el usuario
    if temp > temp_alta:
        temp_alta = temp_total
    if temp <= temp_baja:
        temp_baja = temp_total
#Se saca el promedio de la temperatura
temp_promedio = temp_total/temp_cant
#Finalmente se muestra en la pantalla un mensaje el cual nos dice cuales son la temperatura mas alta y baja que dijito el usuario y el promedio de temperatura :)
print(f"La temperatura mas alta es {temp_alta}, la mas baja es {temp_baja} y la el promedio de la temperatura es {temp_promedio:.1f}.") 
