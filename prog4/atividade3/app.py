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

    nome = str(input())
    texto = mod.lerArquivo(nome)

    print(texto)


if __name__ == "__main__":
    main()