import mod
import sys

def main():

    frase1 = sys.argv[0]
    frase2 = sys.argv[1]

    lista1 = mod.remover_rep(frase1)
    lista2 = mod.remover_rep(frase2)

if __name__ == "__main__":
    main()