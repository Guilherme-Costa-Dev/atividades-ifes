import mod

def main():
        
    lista = mod.lerArquivo()
    lista = mod.transformarEmFloat(lista)
    lista = mod.ordList(lista)
    mod.imprimirDados(lista)
            
if __name__ == "__main__":
    main()