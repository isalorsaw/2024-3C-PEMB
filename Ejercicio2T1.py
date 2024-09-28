#Ingresar tres números e imprima cual es el mayor de ellos.
#Todas las variables involucradas deben de ser declaradas con 0
n1=0
n2=0
n3=0
mayor=0

print("Ingrese el Primer Numero")
n1=int(input())
print("Ingrese el Segundo Numero")
n2=int(input())
print("Ingrese el Tercer Numero")
n3=int(input())

if n1>n2 and n1>n3:
    print("El Mayor es: ",n1)
elif  n2>n1 and n2>n3:
    print ("El Mayor es: ",n2)
elif n3>n1 and n3>n2:
    print ("El Mayor es: ",n3)


