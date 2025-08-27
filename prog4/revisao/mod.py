'''
    Grupo:
        Soul Society
    Integrantes:
        Guilherme Cordeiro Costa
        Fillipy Costa da Silva
        Pablo Nistal Lazaro Santos
'''

def remover_rep(frase:str)->list:
    lista = list(frase)
    lista2 = []
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    return lista2

def uniao(lista1:list, lista2:list)->list:
    lista3 = lista1.copy()
    for i in lista2:
        if i not in lista3:
            lista3.append(i)
    return lista3

def intersecao(lista1:list, lista2:list)->list:
    lista3 = []
    for i in lista1:
        if i in lista2:
            lista3.append(i)
    return lista3
