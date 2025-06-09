def lerArquivo(nome:str)->list:
    with open(nome, 'r', encoding='utf-8') as arquivo:
        listaG = list()
        for linha in arquivo:
            lista = linha.split(",")
            listaG.append(lista)
    arquivo.close()
    return listaG

def compararRespostas(resposta1:list, resposta2:list)->int:
    pts = 0
    tam = len(resposta1)
    for i in range(tam):
        if resposta1[i] == "I" or resposta2[i] == "I":
            pts+=1
        elif resposta1[i] == resposta2[i]:
            pts+=2
    return pts

def compararPont(lista1:list, lista2:list)->list:
    tam = len(lista1)
    listaG = []
    for i in range(tam):
        listaM = []
        pts = compararRespostas(lista1[i][1:], lista2[i][1:])
        listaM.append(lista1[i][0])
        listaM.append(lista2[i][0])
        listaM.append(pts)
        listaG.append(listaM)
    return listaG

def imprimirLista(lista:list)->None:
    tam = len(lista)
    for i in range(tam):
        print("CPF", i, ":", lista[i][0], "Respostas:", lista[i][1:])

def imprimirPar(lista:list)->None:
    tam = len(lista)
    for i in range(tam):
        print("PAR:", lista[i][0], "E", lista[i][1], "PONTUACAO:", lista[i][2])
