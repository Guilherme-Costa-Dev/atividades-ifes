def remover_rep(frase:str)->list:
    lista = list(frase)

    lista2 = []

    for i in lista:
        repetido = False
        for j in lista2:
            if i == j:
                repetido = True
                break
        if repetido == False:
            lista2.append(i)

    return lista2

def uniao(lista1:list, lista2:list)->list:
    lista3 = lista1
    for i in lista2:
        if i in lista3:
            lista3.append(i)
    return lista3