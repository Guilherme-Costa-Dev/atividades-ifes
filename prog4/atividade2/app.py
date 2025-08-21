import mod

def main():

    tam1 = int(input())
    tam2 = int(input())
    lista1 = mod.criarLista(tam1)
    lista2 = mod.criarLista(tam2)

    intercalacao = mod.intercalacaoOrd(lista1, lista2)

    print(lista1, lista2, intercalacao)

if __name__ == "__main__":
    main()