import mod

def main():
        
    lista = mod.lerArquivo()
    print(lista)
    lista = mod.transformarEmFloat(lista)
    print(lista)
    lista = mod.ordList(lista)
    print(lista)
    mod.imprimirDados(lista)
            
if __name__ == "__main__":
    main()