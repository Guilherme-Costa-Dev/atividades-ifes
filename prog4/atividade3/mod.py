'''
    Grupo:
        Soul Society
    Integrantes:
        Guilherme Cordeiro Costa
        Fillipy Costa da Silva
        Pablo Nistal Lazaro Santos
'''

def lerArquivo() -> dict:
    nome = "base.txt"  # nome do arquivo que contém os dados dos produtos
        with open(nome, "r", encoding="utf-8") as arquivo:
        hash = {}  # dicionário que armazenará os produtos
        for i in arquivo:  # lê linha por linha do arquivo
            i = i.strip("\n")  # remove o caractere de quebra de linha
            lista = i.split(";")  # separa os dados da linha por ponto e vírgula
            lista2 = []
            # adiciona todos os elementos da lista exceto o primeiro (nome do produto)
            for j in range(1, len(lista)):
                lista2.append(lista[j])
            hash[lista[0]] = lista2 # adiciona o nome do produto como chave e a lista 2 (todo o resto) como conteudo
            # preço para float
            hash[lista[0]][0] = float(hash[lista[0]][0])
            # quantidade em estoque para int
            hash[lista[0]][1] = int(hash[lista[0]][1])
            # quantidade vendida para int
            hash[lista[0]][2] = int(hash[lista[0]][2])
    arquivo.close() 
    return hash  

def venderProd(hash: dict) -> None:
    prod = str(input())  # lê o nome do produto que será vendido
    while prod != "FIM":  # enquanto não digitar "FIM"
        if prod not in hash:  # verifica se o produto existe no dicionário
            print("PRODUTO INEXISTENTE")  # avisa que produto não foi encontrado
        else:
            qnt = int(input("Digite a quantidade: "))  # lê a quantidade vendida
            # verifica se quantidade é válida (positiva e menor ou igual ao estoque disponível)
            if (qnt > 0) and (qnt <= (hash[prod][1]) - (hash[prod][2])):
                # atualiza a quantidade vendida somando a nova venda
                hash[prod][2] = hash[prod][2] + qnt
            else:
                print("QUANTIDADE INVALIDA")  # avisa que quantidade está inválida
        prod = str(input())  # lê o próximo produto para venda

def imprimirRelatorio(hash: dict) -> None:
    total = 0  # variável para acumular o total vendido em dinheiro
    for i in sorted(hash):  # percorre os produtos em ordem alfabética
        if hash[i][2] > 0:  # só mostra os produtos que tiveram vendas (>0)
            valorProd = hash[i][2] * hash[i][0]  # calcula valor vendido do produto
            # imprime o nome, quantidade vendida e valor total da venda formatado
            print(f"{i:<20}|{hash[i][2]:>8}|{valorProd:<8.2f}")
            total += valorProd  # acumula o valor total vendido
    print(f"TOTAL EM VENDAS = {total:.2f}")  # imprime o total geral de vendas

def arquivoRelatorio(hash: dict) -> None:
    with open("RELATORIO DE VENDAS.txt", "w", encoding="utf-8") as arquivo:
        total = 0  # variável para acumular total vendido
        for i in sorted(hash):  # para cada produto em ordem alfabética
            if hash[i][2] > 0:  # somente produtos com vendas
                valorProd = hash[i][2] * hash[i][0]  # valor vendido no produto
                # escreve a linha formatada no arquivo texto
                arquivo.write(f"{i:<20}|{hash[i][2]:>8}|{valorProd:<8.2f}\n")
                total += valorProd
        # escreve o total geral no arquivo
        arquivo.write(f"TOTAL EM VENDAS = {total:.2f}")

def relatorioRep(hash: dict) -> None:
    # percorre produtos em ordem alfabética
    for i in sorted(hash):
        # verifica se o produto está com estoque zerado após vendas
        if (hash[i][1] - hash[i][2]) == 0:
            print(f"{i:<20}")  # imprime o nome do produto para reposição

def arquivoRelatorioRep(hash: dict) -> None:
    # abre arquivo para escrever os produtos a repor
    with open("REPOSICAO DE ESTOQUE.txt", "w", encoding="utf-8") as arquivo:
        # percorre os produtos
        for i in sorted(hash):
            # verifica se o estoque está zerado
            if (hash[i][1] - hash[i][2]) == 0:
                # escreve o nome do produto no arquivo
                arquivo.write(f"{i:<20}\n")
