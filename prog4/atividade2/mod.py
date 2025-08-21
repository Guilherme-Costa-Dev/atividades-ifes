def criarLista(tam:int)->list:
    lista = []
    for i in range(tam):
        num = int(input())
        lista.append(num)
        lista.sort()
    return lista

def intercalacaoOrd(lista1:list, lista2:list)->list:
    lista3 = []

    i = 0
    j = 0
    while i < len(lista1) and j < len(lista2):
        if lista1[i]<=lista2[j]:
            lista3.append(lista1[i])
            i+=1
        else:
            lista3.append(lista2[j])
            j+=1
    
    while len(lista1)>i:
        lista3.append(lista1[i])
        i+=1
    while len(lista2)>j:
        lista3.append(lista2[j])
        j+=1
        
    return lista3

def imprimirListas(lista:list)->None:
    for i in range(len(lista)):
        print("LISTA[",i,"] = ",lista[i])