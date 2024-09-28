#Ingrese números hasta que se introduzca un cero y enseguida
#mostrar la suma de todos los números ingresados.

numero=0
suma=0
contador=1

print("Ingrese un Numero")
numero=int(input())

while numero!=0:
    suma=suma+numero
    print("Ingrese un Numero")
    numero=int(input())

    
print("La Suma es: ",suma)
