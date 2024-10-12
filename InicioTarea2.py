#Isaias Salinas 232051048
def pedirNumero(msg):
    print(msg)
    num=int(input())
    return num

def crearArreglo(arr,valor):
    arr=[0]*valor

#MAIN=====================================================
arr=[0]*0
tam=pedirNumero("Cual sera el tamanio del arreglo")

menu="Menu\n1.Crear\n2.Rellenar\n3...\n4....\n5...\n6....\n7...."\
      "\n8....\n9.....\n10.....\n11.....\n12....\n13....\n0.Salir";

opcion=pedirNumero(menu)

while opcion!=0:

    if opcion==1:
        crearArreglo(arr,tam)
    
    opcion=pedirNumero(menu)

print("Adios")
