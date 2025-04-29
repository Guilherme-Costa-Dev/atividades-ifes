def calcIMC(peso:float, alt:float)->float:
    return ((peso)/(alt**2))

def ordList(lista:list)->list:
    lista.sort(key = lambda x: calcIMC(x[1], x[2]))
    return lista

def transformarEmFloat(lista:list)->list:
    for i in range(len(lista)):
        index = 1
        while index<len(lista[i]):
            lista[i][index] = float(lista[i][index])
            index+=1

    return lista

def lerArquivo()->list:
    nome = 'dados.txt'
    with open(nome, 'r', encoding='utf-8') as arquivo:
        listaGrande = list()
        for linha in arquivo:
            lista = linha.split(";")
            listaGrande.append(lista)
    arquivo.close()
    return listaGrande

def imprimirDados(lista:list):
    with open("saida.txt", "w", encoding="utf-8") as arquivo:
        for i in range(len(lista)):
            imc = calcIMC(lista[i][1], lista[i][2])
            imc = str(imc)
            arquivo.write(lista[i][0])
            arquivo.write(";")
            arquivo.write(imc)
            arquivo.write("\n")
                