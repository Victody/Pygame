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
    pygame.display.set_caption("Movimentação e Colisão de imagem")
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

    imagem = pygame.image.load('assets\imagem\F117Space.png')
    (x,y) = (150,100)
    obj_velocidade = 5
    vX = 0
    vY= 0

    ret = pygame.Rect(250,300,20,500)

    sprite = pygame.sprite.Sprite()
    sprite.image = imagem
    sprite.rect = imagem.get_rect()
    sprite.rect.top = 50
    sprite.rect.left = 50


    #pygame.font.init()


    #Enquanto o jogo estiver executando
    while onGame:
        for event in pygame.event.get():
        #Capturo um evento e aplico na variável event
            if event.type == pygame.QUIT:
            #Sse o evento for do tipo 'quit', ou seja, o usuário clicar no botão fechar
                onGame = False
                #'Desliga' o jogo

            # Movimento pelo teclado
            if event.type == pygame.KEYDOWN:
                # O primeiro passo é verificar se qualquer tecla foi pressionada
                if event.key == pygame.K_LEFT:
                   vX -= obj_velocidade

                if event.key == pygame.K_RIGHT:
                   vX +=obj_velocidade

                if event.key == pygame.K_UP:
                    vY -=obj_velocidade

                if event.key == pygame.K_DOWN:
                    vY += obj_velocidade
            if event.type == pygame.KEYUP:
                # O primeiro passo é verificar se qualquer tecla foi pressionada
                if event.key == pygame.K_LEFT:
                   vX = 0

                if event.key == pygame.K_RIGHT:
                   vX =0

                if event.key == pygame.K_UP:
                    vY = 0

                if event.key == pygame.K_DOWN:
                    vY = 0

        # if event.type == pygame.MOUSEBUTTONDOWN:

        if sprite.rect.colliderect(ret):
            sprite.rect.left = oldX
            sprite.rect.top = oldY

        x += vX
        y += vY
        relogio.tick(120)
        # tick atualiza a tela a 60 frames por segundo

        tela.fill(cor_branca)

        #tela.blit(imagem,(x-25,y-25))
        #(x,y) = pygame.mouse.get_pos()
        pygame.draw.rect(tela, cor_vermelha, ret)

        oldX = sprite.rect.left
        oldY = sprite.rect.top
        tela.blit(sprite.image, sprite.rect)
        sprite.rect.move_ip(vX, vY)

        pygame.display.update()

    pygame.quit()#Fecha a janela

main()
