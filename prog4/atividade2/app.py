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

    tam1 = int(input())
    tam2 = int(input())
    lista1 = mod.criarLista(tam1)
    lista2 = mod.criarLista(tam2)
    intercalacao = mod.intercalacaoOrd(lista1, lista2)
    mod.imprimirListas(lista1)
    mod.imprimirListas(lista2)
    mod.imprimirListas(intercalacao)
    

if __name__ == "__main__":
    main()