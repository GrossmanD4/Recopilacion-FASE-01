#Programa que capture 3 números positivos, (validar), a los 3 positivos los envía a una función en la que determina y muestra cual es el mayor.
def mayo(n1,n2,n3):
    lista=[n1,n2,n3]
    mayor=max(lista)
    print("El número mayor entre los 3 es ",mayor)

n1=float(input("Ingrese el primero número: "))
while n1<0:
    n1=float(input("Ingrese un número positivo: "))

n2=float(input("Ingrese el segundo número: "))
while n2<0:
    n2=float(input("Ingrese un número positivo: "))

n3=float(input("Ingrese el tercer número: "))
while n3<0:
    n3=float(input("Ingrese un número positivo: "))

mayo(n1,n2,n3)