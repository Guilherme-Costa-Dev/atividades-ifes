import random

def f_buscaBinariaAlterada(lista:list, num:float)->tuple:
    pos = -1
    start = 0
    quant = 0
    end = len(lista)-1
    while start <= end and pos == -1:
        meio = (start+end)//2
        if num == lista[meio]:
            pos = meio
            quant+=1
        else:
            quant+=1
            if num > lista[meio]:
                start = meio+1
            else:
                end = meio-1
    return pos, quant


def f_buscaSequencialAlterada(dados:list, num:float)-> tuple:
    pos = -1
    i = 0
    quant = 0
    while i<len(dados) and pos == -1:
        if dados[i] == num:
            pos = i
        i += 1
        quant += 1
    return pos, quant

def f_preencheListaRand(num:int)->list:
    lista = []
    for i in range(num):
        lista.append(random.random()*100)
    return lista


def f_ordenaCrescente(lista:list)->list:
    lista.sort()
    return lista