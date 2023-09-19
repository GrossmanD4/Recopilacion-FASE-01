#Trabajando con funciones. Elabore un programa que capture dos números por teclado, si son iguales muestra un mensaje; pero si son diferentes, 
#se llama a una función y los envía. En la función muestra cuál es el mayor.
def funcion01(n1,n2):
    if n1==n2:
        print("Son iguales.")
    else:
        if n1>n2:
            print("El mayor es ",n1)
        else:
            print("El mayor es ",n2)

n1=int(input("Ingrese el primer número: "))
n2=int(input("Ingrese el segundo número: "))
funcion01(n1,n2)