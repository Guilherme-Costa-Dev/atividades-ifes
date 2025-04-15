import mod

def main():

  #lista contendo os valores float

  conjunto = list()

  #valores a serem procurados no conjunto

  val1, val2, val3, val4 = float(), float(), float(), float()

  #posições onde os valores foram encontrados pelo algorítmo busca sequencial

  posS1, posS2, posS3 = int(), int(), int()

  #quantidade de comparações que o algoritmo de busca sequencial realizou até encontrar os valores procurados

  contS1, contS2, contS3 = int(), int(), int()

 

  #posições onde os valores foram encontrados pelo algorítmo busca sequencial

  posB1, posB2, posB3 = int(), int(), int()

  #quantidade de comparações que o algoritmo de busca sequencial realizou até encontrar os valores procurados

  contB1, contB2, contB3 = int(), int(), int()

 

  conjunto = mod.f_preencheListaRand(10000)

  val1 = conjunto[0]

  val2 = conjunto[5000]

  val3 = conjunto[9999]

  val4 = -666.66

  conjunto = mod.f_ordenaCrescente(conjunto)

  posS1,contS1 = mod.f_buscaSequencialAlterada(conjunto, val1)

  posS2,contS2 = mod.f_buscaSequencialAlterada(conjunto, val2)

  posS3,contS3 = mod.f_buscaSequencialAlterada(conjunto, val3)

  posS4,contS4 = mod.f_buscaSequencialAlterada(conjunto, val4)

  print("posS1 =",posS1, "contS1 =", contS1)

  print("posS2 =",posS2, "contS2 =", contS2)

  print("posS3 =",posS3, "contS3 =", contS3)

  print("posS4 =",posS4, "contS4 =", contS4)

  posB1,contB1 = mod.f_buscaBinariaAlterada(conjunto, val1)

  posB2,contB2 = mod.f_buscaBinariaAlterada(conjunto, val2)

  posB3,contB3 = mod.f_buscaBinariaAlterada(conjunto, val3)

  posB4,contB4 = mod.f_buscaBinariaAlterada(conjunto, val4)

  print("posB1 =",posB1, "contB1 =", contB1)

  print("posB2 =",posB2, "contB2 =", contB2)

  print("posB3 =",posB3, "contB3 =", contB3)

  print("posB4 =",posB4, "contB4 =", contB4)


if __name__ == "__main__":
  main()

