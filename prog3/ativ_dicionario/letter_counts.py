import sys

def main():

    frase = sys.argv[1]
    hash = {}

    for letra in frase:
        letra = letra.lower()
        if letra.isalpha(): 
            if letra in hash:
                hash[letra] += 1
            else:
                hash[letra] = 1

    for letra in sorted(hash):
        print(letra, hash[letra])

if __name__ == "__main__":
    main()