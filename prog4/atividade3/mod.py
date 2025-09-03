'''
    Grupo:
        Soul Society
    Integrantes:
        Guilherme Cordeiro Costa
        Fillipy Costa da Silva
        Pablo Nistal Lazaro Santos
'''

def lerArquivo()->dict:
    nome = "produtos.txt"
    with open(nome, "r", encoding="utf-8") as arquivo:
        hash = {}
        for i in arquivo:
            i = i.strip("\n")
            lista = i.split(";")
            lista2 = []
            for j in range(1, len(lista)):
                lista2.append(lista[j])
            hash[lista[0]] = lista2
            hash[lista[0]][0] = float(hash[lista[0]][0])
            hash[lista[0]][1] = int(hash[lista[0]][1])
            hash[lista[0]][2] = int(hash[lista[0]][2])
    arquivo.close()
    return hash

def venderProd(hash:dict)->None:
    prod = str(input())
    while prod != "FIM":
        if prod not in hash:
            print("PRODUTO INEXISTENTE")
        else:
            qnt = int(input("Digite a quantidade: "))
            if (qnt > 0) and (qnt <= (hash[prod][1])-(hash[prod][2])):
                hash[prod][2] = hash[prod][2] + qnt
            else:
                print("QUANTIDADE INVALIDA")
        prod = str(input())

def imprimirRelatorio(hash:dict)->None:
    total = 0
    for i in sorted(hash):
        if hash[i][2] > 0:
            valorProd = hash[i][2] * hash[i][0]
            print(f"{i:<20}|{hash[i][2]:>8}|{valorProd:<8.2f}")
            total += valorProd
    print(f"TOTAL EM VENDAS = {total:.2f}")

def arquivoRelatorio(hash:dict)->None:
    with open("RELATORIO DE VENDAS.txt", "w", encoding="utf-8") as arquivo:
        total = 0
        for i in sorted(hash):
            if hash[i][2]>0:
                valorProd = hash[i][2] * hash[i][0]
                arquivo.write(f"{i:<20}|{hash[i][2]:>8}|{valorProd:<8.2f}\n")
                total += valorProd
        arquivo.write(f"TOTAL EM VENDAS = {total:.2f}")

def relatorioRep(hash:dict)->None:
    for i in sorted(hash):
        if (hash[i][1] - hash[i][2]) == 0:
            print(f"{i:<20}")