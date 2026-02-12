import sys, mod

def main(): 

    nome1 = sys.argv[1]
    nome2 = sys.argv[2]
    lista1 = mod.lerArquivo(nome1)
    lista2 = mod.lerArquivo(nome2)
    mod.imprimirLista(lista1)
    mod.imprimirLista(lista2)
    pts = mod.compararPont(lista1, lista2)
    mod.imprimirPar(pts)

if __name__ == "__main__":
    main()