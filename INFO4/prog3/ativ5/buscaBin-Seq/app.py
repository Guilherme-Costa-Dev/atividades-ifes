import mod

def main():

    lista = [10,20,30,40,50,60,70,80,90]
    pos = mod.buscaBin(lista, 30)
    print(pos)
    posSeq = mod.buscaSeq(lista, 40)
    print(posSeq)

if __name__ == "__main__":
    main()