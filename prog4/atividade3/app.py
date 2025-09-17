'''
    Grupo:
        Soul Society
    Integrantes:
        Guilherme Cordeiro Costa
        Fillipy Costa da Silva
        Pablo Nistal Lazaro Santos
'''

import mod  # importa o arquivo mod

def main():
    # chama a função para ler o arquivo e obter o dicionário de produtos
    prod = mod.lerArquivo()
    # inicia o processo de vendas (entrada dos produtos a serem vendidos)
    mod.venderProd(prod)
    # imprime o relatório de vendas no console
    mod.imprimirRelatorio(prod)
    # salva o relatório de vendas em arquivo texto
    mod.arquivoRelatorio(prod)
    # imprime no console os produtos que precisam ser repostos
    mod.relatorioRep(prod)
    # salva em arquivo texto os produtos para reposição
    mod.arquivoRelatorioRep(prod)

if __name__ == "__main__":
    main()
