import pygame

def main():
    # As Definições dos objetos

    screen_width = 600
    screen_height = 450
    # variáveis para tamanho de tela

    pygame.init()
    # Iniciando a biblioteca


    tela = pygame.display.set_mode([screen_width, screen_height])
    # Defini o tamanho de Tela
    pygame.display.set_caption("Jogo Colisão com Retângulo")
    # Defini Texto da janela

    relogio = pygame.time.Clock()
    # Clock captura o tempo de atualização da tela

    onGame = True
    # variável para controlar a execução do jogo

    cor_branca = (255, 255, 255)
    cor_preta = (5, 5, 5)
    cor_azul = (108, 194, 236)
    cor_verde = (54, 182, 112)
    cor_vermelha = (227, 57, 9)
    # variável com código RGB

    sup = pygame.Surface((screen_width, screen_height))
    sup.fill(cor_preta)

    ret = pygame.Rect(10, 10, 22, 32)
    imagem = pygame.image.load('assets\imagem\DiretorMorte (1).png')
    (x, y) = (10, 10)
    pygame.mouse.set_pos(10, 10)
    # Definições do retângulo jogador(pos X, pos y, largura, altura)
    ret2 = pygame.Rect(0, 40, 560, 20)
    # Definições do retângulo (pos X, pos y, largura, altura)
    ret3 = pygame.Rect(100, 100, 500, 20)
    # Definições do retângulo (pos X, pos y, largura, altura)
    ret4 = pygame.Rect(0, 100, 50, 20)
    # Definições do retângulo (pos X, pos y, largura, altura)
    ret5 = pygame.Rect(0, 160, 560, 20)
    # Definições do retângulo (pos X, pos y, largura, altura)
    ret6 = pygame.Rect(100, 220, 500, 20)
    # Definições do retângulo (pos X, pos y, largura, altura)
    ret7 = pygame.Rect(0, 220, 50, 20)
    # Definições do retângulo (pos X, pos y, largura, altura)
    ret8 = pygame.Rect(0, 290, 560, 20)
    # Definições do retângulo (pos X, pos y, largura, altura)



    pygame.font.init()
    # Faz a pygame inicializar a classe de fontes

    fonte_perdeu = pygame.font.Font('assets/fonts/emulogic.ttf', 35)
    fonte_ganhou = pygame.font.Font('assets/fonts/emulogic.ttf', 30)

    audio_explosao = pygame.mixer.Sound('assets/audio/399303__dogfishkid__explosion-012.ogg')

    while onGame:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                onGame = False

            if event.type == pygame.MOUSEBUTTONDOWN:
            # Captura evento de click do mouse
                pygame.mouse.set_pos(10, 10)
                main()
                #Seta a posição do mouse no centro da tela

            if event.type == pygame.KEYDOWN:
            #O primeiro passo é verificar se qualquer tecla foi pressionada
                if event.key == pygame.K_LEFT:
                #Se a tecla direcional esquerda estiver pressionada
                    ret.move_ip(-10,0)
                    #movimenta o retângulo para esquerda(_ip captura o teclado)

        relogio.tick(30)
        # tick atualiza a tela a 60 frames por segundo
        tela.fill(cor_branca)
        # Preencho a tela com a cor branca
        tela.blit(sup, [0, 0])
        # o comando blit adiciona a superfície

        (xant, yant) = (ret.left, ret.top)  # Captura posiçãp do objeto antes da colisão
        (ret.left, ret.top) = pygame.mouse.get_pos()  # define a posição do retângulo no mouse
        ret.left -= (ret.width / 2)  # Define o centro do retângulo como o centro de sua largura (posição do mouse)
        ret.top -= ret.height / 2  # Define o centro do                                                                                                                                                                          objeto no cento de sua altura

        if ret.colliderect(ret2) or ret.colliderect(ret3)or ret.colliderect(ret4)or ret.colliderect(ret5)or ret.colliderect(ret6)or ret.colliderect(ret7)or ret.colliderect(ret8):  # Se houver colisão com outro objeto
            text = fonte_perdeu.render('PERDEU!', 1, cor_verde)
            tela.blit(text, [150, 400])
            audio_explosao.play()
            audio_explosao.set_volume(0.5)
            (ret.left, ret.top) = (xant, yant)# define a posição do objeto para a posição anterior a colisão
            pygame.mouse.set_pos(10, 10)
        if ret.top > 400:
            text = fonte_perdeu.render('VENCEU!', 1, cor_verde)
            tela.blit(text, [150, 200])
            text = fonte_ganhou.render('Clique para iniciar!', 1, cor_vermelha)
            tela.blit(text, [5, 300])
            ret2.left = 602
            ret3.left = 602
            ret4.left = 602
            ret5.left = 602
            ret6.left = 602
            ret7.left = 603
            ret8.left = 603


        pygame.draw.rect(tela, cor_preta, ret)  # Desenha retangulo
        pygame.draw.rect(tela, cor_branca, ret2)  # Desenha retangulo
        pygame.draw.rect(tela, cor_branca, ret3)  # Desenha retangulo
        pygame.draw.rect(tela, cor_branca, ret4)  # Desenha retangulo
        pygame.draw.rect(tela, cor_branca, ret5)  # Desenha retangulo
        pygame.draw.rect(tela, cor_branca, ret6)  # Desenha retangulo
        pygame.draw.rect(tela, cor_branca, ret7)
        pygame.draw.rect(tela, cor_branca, ret8)
        tela.blit(imagem, ((ret.left-5), ret.top))
        (x, y) = ((ret.left-5), ret.top)
        pygame.display.update()  # Atualizações da tela

    pygame.quit()  # Fecha a janela

main()

