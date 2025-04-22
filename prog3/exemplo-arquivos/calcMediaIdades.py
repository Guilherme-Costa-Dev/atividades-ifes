def main():

    nome = "idade.txt"

    with open(nome, 'r', encoding='utf-8') as arq_entrada:
        # CORPO DO WITH
        conteudo = arq_entrada.read()

    # continue o programa usando conteudo
    lista = conteudo.split()
    total = 0
    index = 0
    for i in range(len(lista)):
        lista[i] = int(lista[i])
        total += lista[i]
        index += 1
    media = total/index

    print(media)

if __name__ == "__main__":
    main()