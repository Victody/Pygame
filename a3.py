import pygame
import random


def main():
    #Definições dos objetos

    screen_width = 600
    screen_height = 600
    #variáveis para tamanho de tela

    pygame.init()
    #Iniciando a biblioteca

    tela = pygame.display.set_mode([screen_width, screen_height])
    #Defini o tamanho de Tela
    pygame.display.set_caption("Imagens")
    #Defini Texto da janela

    relogio = pygame.time.Clock()
    #Clock captura o tempo de atualização da tela

    onGame = True
    #variável para controlar a execução do jogo

    cor_branca = (255,255,255)
    cor_azul = (108,194,236)
    cor_verde = (54,182,112)
    cor_vermelha = (227,57,9)
    # variável com código RGB

    imagem = pygame.image.load('assets\imagem\DiretorMorte (1).png')
    (x,y) = (150,100)

    ret = pygame.Rect(250,300,20,500)

    #pygame.font.init()


    #Enquanto o jogo estiver executando
    while onGame:
        for event in pygame.event.get():
        #Capturo um evento e aplico na variável event
            if event.type == pygame.QUIT:
            #Sse o evento for do tipo 'quit', ou seja, o usuário clicar no botão fechar
                onGame = False
                #'Desliga' o jogo

            #if event.type == pygame.MOUSEBUTTONDOWN:

        relogio.tick(120)
        # tick atualiza a tela a 60 frames por segundo
        tela.fill(cor_branca)
        tela.blit(imagem,(x,y))
        (x,y) = pygame.mouse.get_pos()
        pygame.draw.rect(tela, cor_vermelha, ret)
        pygame.display.update()

    pygame.quit()#Fecha a janela

main()
