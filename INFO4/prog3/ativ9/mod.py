def transformarEmFloat(lista:list)->list:
    for i in range(len(lista)):
        index = 1
        while index<len(lista[i]):
            lista[i][index] = float(lista[i][index])
            index+=1
    return lista

def lerArquivo(nome:str)->list:
    with open(nome, 'r', encoding='utf-8') as arquivo:
        listaG = list()
        for linha in arquivo:
            lista = linha.split(";")
            listaG.append(lista)
    arquivo.close()
    return listaG

def transformarEmFloat(lista:list)->list:
    tam = len(lista)
    for i in range(tam):
        j = 6
        while j<len(lista[i]):
            lista[i][j] = float(lista[i][j])
            j+=1
    return lista

def somarTotalDoAno(lista:list)->list:
    tam = len(lista)
    for i in range(tam):
        soma = 0
        j = 6
        while j<len(lista[i]):
            soma += lista[i][j]
            j+=1
        lista[i] = soma
    return lista

def imprimirDados(lista:list, num:int):
    tam = len(lista)
    if num == 0:
        print("MULHERES")
    else:
        print("HOMENS")

    for i in range(tam):
        print("IDADE=",i,"QTD=",int(lista[i]))

def criarArquivo(h:list, m:list):
    with open("saida.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("MULHERES\n")
        for i in range(len(m)):
            arquivo.write("IDADE=")
            arquivo.write(str(i))
            arquivo.write(" QTD=")
            arquivo.write(str(int(m[i])))
            arquivo.write("\n")
        arquivo.write("HOMENS\n")
        for i in range(len(h)):
            arquivo.write("IDADE=")
            arquivo.write(str(i))
            arquivo.write(" QTD=")
            arquivo.write(str(int(h[i])))
            arquivo.write("\n")