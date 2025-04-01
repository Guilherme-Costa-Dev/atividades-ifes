import mod
def main():

    num = int(input())
    lista = mod.preencherLista(num)
    ordLista = mod.ordList(lista)
    mod.printList(ordLista)

if __name__ == "__main__":
    main()