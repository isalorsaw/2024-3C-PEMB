#Funcion que pide un numero y lo retorna
def pedirNumero(msg):
    print(msg)
    numero=int(input())
    return numero

#Metodo que recibe un mensaje y lo muestra en pantalla
def mostrar(msg):
    print(msg)

#Metodo que imprime un Arreglo
def imprimir(titulo,arr):
    print(arr)

#Metodo llenar arreglo por usuario
def llenarArreglo(arr):
    i=0
    while(i<len(arr)):
        arr[i]=pedirNumero("Ingrese un Numero")
        i=i+1;

#MAIN===========================================================
tam=pedirNumero("Ingrese el Tamanio del Arreglo");
arreglo=[0]*tam
print("\nLos elementos del arreglo: \n",arreglo)
llenarArreglo(arreglo)
imprimir("Elementos del Arreglo",arreglo)
