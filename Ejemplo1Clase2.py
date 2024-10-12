#Funcion que pide un numero y lo retorna
def pedirNumero(msg):
    print(msg)
    numero=int(input())
    return numero

#Metodo que recibe un mensaje y lo muestra en pantalla
def mostrar(msg):
    print(msg)

#MAIN===========================================================
num1=pedirNumero("Ingrese un Numero")
num2=pedirNumero("Ingrese otro Numero")
suma=num1+num2
mostrar("La suma es: "+str(suma))
