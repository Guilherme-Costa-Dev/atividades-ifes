def preencherLista(num:int)->list:
    lista = list()
    lista_menor = list()
    for i in range(num):
        nome = str(input())
        peso = float(input())
        altura = float(input())

        lista_menor.append(nome)
        lista_menor.append(peso)
        lista_menor.append(altura)
        lista.append(lista_menor)
        lista_menor = []
    return lista

def calcIMC(peso:float, alt:float)->float:
    return ((peso)/(alt**2))

def ordList(lista:list)->list:
    lista.sort(key= lambda x: calcIMC(x[1], x[2]))
    return lista

def printList(lista:list)->None:
    for i in range(len(lista)):
        print(f"{lista[i][0]} {calcIMC(lista[i][1], lista[i][2]):.2f}")