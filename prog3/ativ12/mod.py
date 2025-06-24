def lerArquivo(nome:str)->dict:
    with open(nome, 'r', encoding='utf-8') as arquivo:
        hash = {}
        for linha in arquivo:
            lista = linha.strip().split(",")
            hash[lista[0]] = lista[1:]
    arquivo.close()
    return hash

def compararRespostas(resposta1:list, resposta2:list)->int:
    pts = 0
    tam = len(resposta1)
    for i in range(tam):
        if resposta1[i] == "I" or resposta2[i] == "I":
            pts+=1
        elif resposta1[i] == resposta2[i]:
            pts+=2
    return pts

def compararPont(hash1:dict, hash2:dict)->dict:
    hash = {}
    for cpf in hash1:
        for cpf2 in hash2:
            pts = compararRespostas(hash1[cpf], hash2[cpf2])
            tupla = (cpf, cpf2)
            hash[tupla] = pts
    return hash

def printarPessoas(hash:dict)->None:
    index = 1
    for cpf in hash:
        print("CPF", index,":", cpf, "RESPOSTAS:", hash[cpf])
        index+=1

def printarPts(hash:dict)->None:
    for duplas in hash:
        print("PAR",duplas[0],"E", duplas[1], "PONTUACAO",hash[duplas])
    

