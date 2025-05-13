import mod

def main():

    h = mod.lerArquivo("Homens.csv")
    m = mod.lerArquivo("Mulheres.csv")
    h = mod.transformarEmFloat(h)
    m = mod.transformarEmFloat(m)
    h = mod.somarTotalDoAno(h)
    m = mod.somarTotalDoAno(m)
    mod.imprimirDados(m,0)
    mod.imprimirDados(h,1)
    mod.criarArquivo(h,m)

    

if __name__ == "__main__":
    main()