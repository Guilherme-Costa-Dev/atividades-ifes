import mod
def main():

    nome = str(input())
    nome2 = str(input())
    lista1 = mod.lerArquivo(nome)
    lista2 = mod.lerArquivo(nome2)
    print(lista1)
    print(lista2)
    listaComp = mod.compararPont(lista1, lista2)
    print(listaComp)


if __name__ == "__main__":
    main()