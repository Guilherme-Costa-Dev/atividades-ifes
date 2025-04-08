def buscaBin(lista:list, num:float)->int:
    pos = -1
    start = 0
    end = len(lista)-1
    while start <= end and pos == -1:
        meio = (start+end)//2
        if num == lista[meio]:
            pos = meio
        else:
            if num > lista[meio]:
                start = meio+1
            else:
                end = meio-1
    return pos


def buscaSeq(dados:list, num:float)-> int:
    pos = -1
    i = 0
    while i<len(dados) and pos == -1:
        if dados[i] == num:
            pos = i
        i += 1
    return pos