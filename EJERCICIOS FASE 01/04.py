def mayor(n1,n2):
    if n1>n2:
        print("Mayor: ",n1)
    else:
        print("Mayor: ",n2)

a=b=0
while a==b:
    a=int(input("Ingrese el 1er número: "))
    b=int(input("Ingrese el 2do número: "))
mayor(a,b)