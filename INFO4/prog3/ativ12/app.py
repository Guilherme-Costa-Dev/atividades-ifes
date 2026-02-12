import mod
import sys

def main():
    nome1 = sys.argv[1]
    nome2 = sys.argv[2]
    hash1 = mod.lerArquivo(nome1)
    hash2 = mod.lerArquivo(nome2)
    mod.printarPessoas(hash1)
    mod.printarPessoas(hash2)
    print(hash1)
    print(hash2)
    pts = mod.compararPont(hash1, hash2)
    mod.printarPts(pts)
    print(pts)
if __name__ == "__main__":
    main()