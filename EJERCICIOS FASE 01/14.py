#Programa que captura dos números diferentes, los envía a un método de la clase mini, en la cual muestra el menor valor.
class mini:
    def menor(n1,n2):
        if n1==n2:
            print("Son números iguales.")
        else:
            lista=[n1,n2]
            print("El menor entre los dos es ",min(lista))

n1=float(input("Ingrese el primero número: "))
n2=float(input("Ingrese el segundo número: "))

mini.menor(n1,n2)