'''
    Grupo:
        Soul Society
    Integrantes:
        Guilherme Cordeiro Costa
        Fillipy Costa da Silva
        Pablo Nistal Lazaro Santos
'''

import mod

def main():

    frase1 = str(input())
    frase2 = str(input())

    lista1 = mod.remover_rep(frase1)
    lista2 = mod.remover_rep(frase2)
    lista3 = mod.uniao(lista1, lista2)
    lista4 = mod.intersecao(lista1, lista2)

    lista5 = []
    lista5.append(sorted(lista1))
    lista5.append(sorted(lista2))
    lista5.append(sorted(lista3))
    lista5.append(sorted(lista4))

    lista6 = []
    for i in range(len(lista5)):
        sublista = []
        for j in lista5[i]:
            sublista.append(j.upper())
        lista6.append(sublista)
    
    for i in lista6:
        print(i)

if __name__ == "__main__":
    main()