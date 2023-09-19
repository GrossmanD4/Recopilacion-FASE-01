#Programa que convierte radianes en grados. Debe ingresar una cantidad de radianes y muestra resultado en grados.
def radgrad(radianes):
    grados=(radianes*180)/3.14
    print("",radianes," radianes en grados son: ",grados)

radi=float(input("Ingrese los radianes a convertir: "))
radgrad(radi)