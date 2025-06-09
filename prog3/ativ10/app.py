import mod
import sys
def main():

    nome1 = sys.argv[1]
    nome2 = sys.argv[2]
    lista1 = mod.lerArquivo(nome1)
    lista2 = mod.lerArquivo(nome2)
    print(lista1)
    print(lista2)
    listaComp = mod.compararPont(lista1, lista2)
    print(listaComp)


if __name__ == "__main__":
    main()