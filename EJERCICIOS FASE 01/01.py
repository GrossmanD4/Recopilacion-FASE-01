#Haga un programa que capture por teclado dos números, si son iguales, muestra mensaje y termina. Si son diferentes, muestra el mayor, caso contrario, muestra mensaje y termina:
n1=int(input("Ingrese el primer número: "))
n2=int(input("Ingrese el segundo número: "))
if n1==n2:
    print("Son iguales.")
else:
    if n1>n2:
        print("El mayor es ",n1)
    else:
        print("El mayor es ",n2)