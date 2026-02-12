def lerArquivo(nome:str)->list:
    with open(nome, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
        arquivo.close()

        texto = texto.lower()

        texto_sem_pts = ""
        for letra in texto:
            if letra.isalpha() or letra.isspace():
                texto_sem_pts += letra
        texto_sem_pts = texto_sem_pts.split()
        
    return texto_sem_pts

def main():

    texto = lerArquivo("alices_book.txt")
    hash = {}
    for palavra in texto:
        if palavra in hash:
            hash[palavra] += 1
        else:
            hash[palavra] = 1

    for palavra in sorted(hash):
        print(palavra, hash[palavra])

    maior_chave = max(hash, key=hash.get)

    print("A palavra alice aparece", hash["alice"])
    print("A maior palavra e: ", max(hash.keys(), key=len))
    

if __name__ == "__main__":
    main()
