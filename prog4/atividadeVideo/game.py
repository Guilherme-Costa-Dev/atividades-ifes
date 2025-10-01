import pygame as pg

pg.init()

tamanho_tela = (800, 800)
tela = pg.display.set_mode(tamanho_tela)
pg.display.set_caption("Quebra Muros")

tamanho_bola = 15
bola = pg.Rect(100, 500, tamanho_bola, tamanho_bola)
tamanho_jogador = 100
jogador = pg.Rect(0, 750, tamanho_jogador)

qtd_blocos_linha = 8
qtd_linhas_blocos = 5
qtd_total_blocos = qtd_blocos_linha * qtd_blocos_linha * qtd_linhas_blocos

def criar_blocos(qtd_blocos_linha, qtd_linhas_blocos):
    blocos = []

    return blocos

cores = {
    "branca": (255,255,255),
    "preta": (0,0,0),
    "amarela": (255,255,0),
    "azul": (0,0,255),
    "verde": (0,255,0)
}

fim_jogo = False
pontuacao = 0
mov_bola = [1,1]

tela.fill(cores["preta"])

while not fim_jogo:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            fim_jogo = True