import pygame
import sys
import tkinter
import random
from pygame.locals import *  #Essas imports que não estão sendo utilizados, são apenas para salvar para projetos futuros.
import kivy 
from kivy.app import App
from kivy.uix.label import Label
from pygame.constants import QUIT

largura = 800
altura = 600


class jogadores(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.Imagemx = pygame.image.load('imagens/x.png')
        #self.rect = self.Imagemx.get_rect()
        #self.rect.centerx = largura / 2
        #self.rect.centery = altura - 100

    def posicao(self):
        pass

    # coloca o objeto na tela
    def colocar(self, superficie):
        superficie.blit(self.Imagemx, self.rect)


def Velha():
    pygame.init()
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Jogo da Velha")

    jogador1 = jogadores()
    Imagemfundo = pygame.image.load('imagens/fundo.jpg')
    ImagemVelha = pygame.image.load('imagens/velha.png')
    ImagemX = pygame.image.load('imagens/x.png')
    Imagemo = pygame.image.load('imagens/o.png')
    BotaoFechar = pygame.image.load('imagens/fechar.png')
    BotaoFechar2 = pygame.image.load('imagens/fechar2.png')
    BotaoReiniciar = pygame.image.load('imagens/voltar.gif')

    cor_vermelha = (227, 57, 9)
    quad1 = pygame.Rect(240, 120, 90, 90)
    quad2 = pygame.Rect(240, 235, 90, 90)
    quad3 = pygame.Rect(240, 360, 90, 90)
    quad4 = pygame.Rect(360, 120, 90, 90)
    quad5 = pygame.Rect(360, 235, 90, 90)
    quad6 = pygame.Rect(360, 360, 90, 90)
    quad7 = pygame.Rect(480, 120, 90, 90)
    quad8 = pygame.Rect(480, 235, 90, 90)
    quad9 = pygame.Rect(480, 360, 90, 90)

    jogando = True
    LEFT = 1
    RIGHT = 3
    running = 1

    tela.blit(Imagemfundo, (0, 0))
    tela.blit(ImagemVelha, (225, 100))
    tela.blit(BotaoFechar, (670, 500))
    #tela.blit(BotaoReiniciar, (670, 50))
    #tela.blit(BotaoReiniciar, (225, 100))
    #pygame.draw.rect(tela, cor_vermelha, quad1)
    #pygame.draw.rect(tela, cor_vermelha, quad2)
    #pygame.draw.rect(tela, cor_vermelha, quad3)
    #pygame.draw.rect(tela, cor_vermelha, quad4)
    #pygame.draw.rect(tela, cor_vermelha, quad5)
    #pygame.draw.rect(tela, cor_vermelha, quad6)
    #pygame.draw.rect(tela, cor_vermelha, quad7)
    #pygame.draw.rect(tela, cor_vermelha, quad8)
    #pygame.draw.rect(tela, cor_vermelha, quad9)

    pygame.font.init()
    fonte_padrao = pygame.font.get_default_font()
    fonte_inicio = pygame.font.SysFont(fonte_padrao, 45)
    fonte_ganhou = pygame.font.SysFont(fonte_padrao, 30)



    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()


        text = fonte_inicio.render('Ola, Vamos Jogar!', 1, (255, 255, 255))
        tela.blit(text, (25, 25))

                # PRIMEIRO QUADRANTE

        mouse = pygame.mouse.get_pos()
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == LEFT\
            and 240 + 90 > mouse[0] > 240 and 120 + 90 > mouse[1] > 120:
                tela.blit(ImagemX, (240, 120))
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == RIGHT\
            and 240 + 90 > mouse[0] > 240 and 120 + 90 > mouse[1] > 120:
                   tela.blit(Imagemo, (240, 120))


                # SEGUNDO QUADRANTE

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == LEFT\
            and 240 + 90 > mouse[0] > 240 and 235 + 90 > mouse[1] > 235:
                tela.blit(ImagemX, (240, 235))
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == RIGHT\
            and 240 + 90 > mouse[0] > 240 and 235 + 90 > mouse[1] > 235:
                   tela.blit(Imagemo, (240, 235))


                   # TERCEIRO QUADRANTE

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == LEFT \
                and 240 + 90 > mouse[0] > 240 and 360 + 90 > mouse[1] > 360:
                tela.blit(ImagemX, (240, 360))
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == RIGHT \
                and 240 + 90 > mouse[0] > 240 and 360 + 90 > mouse[1] > 360:
                   tela.blit(Imagemo, (240, 360))

                   # QUARTO QUADRANTE

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == LEFT \
                and 360 + 90 > mouse[0] > 360 and 120 + 90 > mouse[1] > 120:
                tela.blit(ImagemX, (360, 120))
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == RIGHT \
                and 360 + 90 > mouse[0] > 360 and 120 + 90 > mouse[1] > 120:
                   tela.blit(Imagemo, (360, 120))

                   # QUINTO QUADRANTE

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == LEFT \
                and 360 + 90 > mouse[0] > 360 and 235 + 90 > mouse[1] > 235:
                tela.blit(ImagemX, (360, 235))
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == RIGHT \
                and 360 + 90 > mouse[0] > 360 and 235 + 90 > mouse[1] > 235:
                tela.blit(Imagemo, (360, 235))

                # SEXTO QUADRANTE

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == LEFT \
                and 360 + 90 > mouse[0] > 360 and 360 + 90 > mouse[1] > 360:
                tela.blit(ImagemX, (360, 360))
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == RIGHT \
                and 360 + 90 > mouse[0] > 360 and 360 + 90 > mouse[1] > 360:
                tela.blit(Imagemo, (360, 360))

                # SETIMO QUADRANTE

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == LEFT \
                and 480 + 90 > mouse[0] > 480 and 120 + 90 > mouse[1] > 120:
                tela.blit(ImagemX, (480, 120))
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == RIGHT \
                and 480 + 90 > mouse[0] > 480 and 120 + 90 > mouse[1] > 120:
                tela.blit(Imagemo, (480, 120))

                # OITAVO QUADRANTE

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == LEFT \
                and 480 + 90 > mouse[0] > 480 and 235 + 90 > mouse[1] > 235:
                tela.blit(ImagemX, (480, 235))
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == RIGHT \
                and 480 + 90 > mouse[0] > 480 and 235 + 90 > mouse[1] > 235:
                tela.blit(Imagemo, (480, 235))

                    # NONO QUADRANTE

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == LEFT \
                and 480 + 90 > mouse[0] > 480 and 360 + 90 > mouse[1] > 360:
                    tela.blit(ImagemX, (480, 360))
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == RIGHT\
                and 480 + 90 > mouse[0] > 480 and 360 + 90 > mouse[1] > 360:
                    tela.blit(Imagemo, (480, 360))

        if 670 + 60 > mouse[0] > 670 and 500 + 60 > mouse[1] > 500:
            tela.blit(BotaoFechar2, (670, 500))
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == LEFT:
                pygame.quit()
                sys.exit()



        # jogador1.colocar(tela)
        pygame.display.update()




Velha()
