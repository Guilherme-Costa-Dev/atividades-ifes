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

    prod = mod.lerArquivo()
    mod.venderProd(prod)
    mod.imprimirRelatorio(prod)
    mod.arquivoRelatorio(prod)
    mod.relatorioRep(prod)
    mod.arquivoRelatorioRep(prod)

if __name__ == "__main__":
    main()