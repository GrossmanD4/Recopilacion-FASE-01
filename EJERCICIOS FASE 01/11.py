#Realizar un programa que captura un numero entre 1 y 7. Si ingresa otro número sigue pidiendo, luego muestra el día de la semana que corresponda.
dias={1:"Lunes",2:"Martes",3:"Miércoles",4:"Jueves",5:"Viernes",6:"Sabado",7:"Domingo"}
num=float(input("Ingrese un número del 1 al 7 --> "))
while num not in dias.keys():
    print("Ingrese un número válido")
    num=float(input("--> "))
print("El día correspondiente a ",num," es ",dias[num])