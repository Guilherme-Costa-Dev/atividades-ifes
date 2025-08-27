'''
    Grupo:
        Soul Society
    Integrantes:
        Guilherme Cordeiro Costa
        Fillipy Costa da Silva
        Pablo Nistal Lazaro Santos
'''

def lerArquivo(nome:str)->hash:
    with open(nome, "r", encoding="utf-8") as arquivo:
        hash = {}
        for i in arquivo:
            lista = i.split(";")
            lista2 = []
            for j in range(1, len(lista)):
                lista2.append(lista[j])
            hash[lista[0]] = lista2
    arquivo.close()
    return hash