'''
    Grupo:
        Soul Society
    Integrantes:
        Guilherme Cordeiro Costa
        Fillipy Costa da Silva
        Pablo Nistal Lazaro Santos
'''

def lerArquivo()->dict:
    nome = "base.txt"
    with open(nome, "r", encoding="utf-8") as arquivo:
        hash = {}
        for i in arquivo:
            i = i.strip("\n")
            lista = i.split(";")
            lista2 = []
            for j in range(1, len(lista)):
                lista2.append(lista[j])
            hash[lista[0]] = lista2
    arquivo.close()
    return hash

def venderProd(hash:dict)->None:
    prod = str(input())
    while prod != "FIM":
        if prod not in hash:
            print("PRODUTO INEXISTENTE")
        else:
            qnt = int(input("Digite a quantidade: "))
            if (qnt > 0) and (qnt < (hash[prod][1])-(hash[prod][2])):
                hash[prod][2] = hash[prod][2] + qnt
            else:
                print("QUANTIDADE INVALIDA")
        prod = str(input())