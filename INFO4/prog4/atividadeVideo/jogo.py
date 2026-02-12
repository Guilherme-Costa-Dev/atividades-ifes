'''
    Integrantes do grupo: Guilherme Cordeiro Costa, Fillipy Costa e Pablo Nistal.
    Grupo: Soul Society
'''

import pygame

# constantes
class Const:
    TAMANHO_TELA = (800, 800)
    TAMANHO_BOLA = 30
    TAMANHO_JOGADOR = 200
    ALTURA_JOGADOR = 15
    QTD_BLOCOS_LINHA = 8
    QTD_LINHAS_BLOCOS = 6
    DISTANCIA_BLOCOS = 5
    ALTURA_BLOCO = 15
    DISTANCIA_ENTRE_LINHAS = 25  # 15 + 10 (altura bloco + espaço)
    MOVIMENTO_BOLA_INICIAL = [2, -2]
    VELOCIDADE_JOGADOR = 3

    CORES = {
        "branca": (255, 255, 255),
        "preta": (0, 0, 0),
        "amarela": (255, 255, 0),
        "azul": (0, 0, 255),
        "verde": (0, 255, 0)
    }

# inicializar
pygame.init()

tela = pygame.display.set_mode(Const.TAMANHO_TELA)
pygame.display.set_caption("Quebra Muros")

bola = pygame.Rect(100, 500, Const.TAMANHO_BOLA, Const.TAMANHO_BOLA)
jogador = pygame.Rect(0, 750, Const.TAMANHO_JOGADOR, Const.ALTURA_JOGADOR)

qtde_blocos_linha = Const.QTD_BLOCOS_LINHA
qtde_linhas_blocos = Const.QTD_LINHAS_BLOCOS
qtde_total_blocos = qtde_blocos_linha * qtde_linhas_blocos

movimento_bola = Const.MOVIMENTO_BOLA_INICIAL.copy()

def criar_blocos():
    altura_tela = Const.TAMANHO_TELA[1]
    largura_tela = Const.TAMANHO_TELA[0]
    distancia_entre_blocos = Const.DISTANCIA_BLOCOS
    largura_bloco = largura_tela / 8 - distancia_entre_blocos
    altura_bloco = Const.ALTURA_BLOCO
    distancia_entre_linhas = altura_bloco + 10

    blocos = []
    for j in range(Const.QTD_LINHAS_BLOCOS):
        for i in range(Const.QTD_BLOCOS_LINHA):
            bloco = pygame.Rect(i * (largura_bloco + distancia_entre_blocos), j * distancia_entre_linhas, largura_bloco, altura_bloco)
            blocos.append(bloco)
    return blocos


fim_jogo = False
pontuacao = 0

def desenhar_inicio_jogo():
    tela.fill(Const.CORES["azul"])
    pygame.draw.rect(tela, Const.CORES["amarela"], jogador)
    pygame.draw.rect(tela, Const.CORES["preta"], bola)

def desenhar_blocos(blocos):
    for bloco in blocos:
        pygame.draw.rect(tela, Const.CORES["verde"], bloco)

def movimentar_jogador(evento):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RIGHT:
            if (jogador.x + Const.TAMANHO_JOGADOR) < Const.TAMANHO_TELA[0]:
                jogador.x = jogador.x + Const.VELOCIDADE_JOGADOR
        if evento.key == pygame.K_LEFT:
            if jogador.x > 0:
                jogador.x = jogador.x - Const.VELOCIDADE_JOGADOR

def movimentar_bola(bola):
    global movimento_bola
    movimento = movimento_bola
    bola.x = bola.x + movimento[0]
    bola.y = bola.y + movimento[1]

    if bola.x <= 0:
        movimento[0] = - movimento[0]
    if bola.y <= 0:
        movimento[1] = - movimento[1]
    if bola.x + Const.TAMANHO_BOLA >= Const.TAMANHO_TELA[0]:
        movimento[0] = - movimento[0]
    if bola.y + Const.TAMANHO_BOLA >= Const.TAMANHO_TELA[1]:
        movimento = None

    if jogador.collidepoint(bola.x, bola.y):
        movimento[1] = - movimento[1]
    for bloco in blocos:
        if bloco.collidepoint(bola.x, bola.y):
            blocos.remove(bloco)
            movimento[1] = - movimento[1]
    return movimento

def atualizar_pontuacao(pontuacao):
    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f"Pontuação: {pontuacao}", 1, Const.CORES["amarela"])
    tela.blit(texto, (0, 780))
    if pontuacao >= qtde_total_blocos:
        return True
    else:
        return False

blocos = criar_blocos()

while not fim_jogo:
    desenhar_inicio_jogo()
    desenhar_blocos(blocos)
    fim_jogo = atualizar_pontuacao(qtde_total_blocos - len(blocos))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True

    movimentar_jogador(evento)

    movimento_bola = movimentar_bola(bola)

    if not movimento_bola:
        fim_jogo = True

    pygame.time.wait(1)
    pygame.display.flip()

pygame.quit()
