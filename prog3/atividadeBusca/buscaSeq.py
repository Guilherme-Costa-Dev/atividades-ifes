def buscaSeq(dados:list, num:float)-> int:
    for i in range(len(dados)):
        if num == dados[i]:
            return i
    return (-1)

def main():

    lista = [10,20,30,40,50]
    pos = buscaSeq(lista, 50)
    print(pos)
    pos = buscaSeq(lista, 20)
    print(pos)

if __name__ == "__main__":
    main()