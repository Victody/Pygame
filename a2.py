import pygame
import random


def main():
    #As Definições dos objetos

    screen_width = 600
    screen_height = 600
    #variáveis para tamanho de tela

    pygame.init()
    #Iniciando a biblioteca

    tela = pygame.display.set_mode([screen_width, screen_height])
    #Defini o tamanho de Tela
    pygame.display.set_caption("Iniciando com Pygame")
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

    sup = pygame.Surface((600,600))
    #Cria uma superfície  com o tamanho de 200 X 200

    ret = pygame.Rect(10,10,100,145)
    #Definições do retângulo (pos X, pos y, largura, altura)
    ret2 = pygame.Rect(50, 50, 145, 100)
    # Definições do retângulo (pos X, pos y, largura, altura)

    pygame.font.init()
    # Faz a pygame inicializar a classe de fontes

    fonte_padrao =  pygame.font.Font('assets/fonts/emulogic.ttf', 35)
    # referenciamos as fontes de maneira exclusiva com os de endereço na pasta e tamanho
    fonte_texto = pygame.font.SysFont('Arial', 30, False, False)
    # referenciamos as fontes de maneira exclusiva com o nome da fonte no sistema, tamanho, construtor, Italico e negrito

    audio_explosao = pygame.mixer.Sound('assets/audio/399303__dogfishkid__explosion-012.ogg')
    #Referência do áudio de explosão com o endereço na pasta raiz do projeto

    listaRet = []
    #Lista para guardar os retângulos aleatórios

    for x in range(15):
        h = random.randrange(20,90)
        w = random.randrange(15,50)
        x = random.randrange(600)
        y = random.randrange(600)
        listaRet.append(pygame.Rect(x,y,w,h))
        #Preenche a lista de retângulos

    #Enquanto o jogo estiver executando
    while onGame:

        for rets in listaRet:
            pygame.draw.rect(sup, cor_azul, rets)
            #desenha cada item da lista de retângulos

        for event in pygame.event.get():
        #Capturo um evento e aplico na variável event
            if event.type == pygame.QUIT:
            #Sse o evento for do tipo 'quit', ou seja, o usuário clicar no botão fechar
                onGame = False
                #'Desliga' o jogo

            #Eventos de mouse
            # if event.type == pygame.MOUSEBUTTONDOWN:#Captura evento de click do moues
            #     #ret = ret.move(10,10)Movimenta o retângulo 10 pixeis para direita e 10 pixeis para baixo
            #     ret = ret.move(10,0)#Movimenta o quadrado no eixo x
            # if event.type == pygame.MOUSEMOTION:
            #     ret = ret.move(0,10)#movimenta quadrado no eico y

            if event.type == pygame.MOUSEBUTTONDOWN:
            #Captura evento de click do mouse
                #pygame.mouse.set_pos(screen_width/2, screen_height/2)
                #Seta a posição do mouse no centro da tela

                if ret.colliderect(ret2):
                    ret2.width = 0
                    ret2.height = 0
                    #Faz o retângulo desaparecer

            #Movimento pelo teclado
            if event.type == pygame.KEYDOWN:
            #O primeiro passo é verificar se qualquer tecla foi pressionada
                if event.key == pygame.K_LEFT:
                #Se a tecla direcional esquerda estiver pressionada
                    ret.move_ip(-10,0)
                    #movimenta o retângulo para esquerda(_ip captura o teclado)

                if event.key == pygame.K_RIGHT:
                #Se a tecla direcional direita estiver pressionada
                    ret.move_ip(10,0)

                if event.key == pygame.K_UP:
                #Se a tecla direcional cima estiver pressionada
                    ret.move_ip(0,-10)

                if event.key == pygame.K_DOWN:
                #Se a tecla direcional baixo estiver pressionada
                    ret.move_ip(0,10)

        relogio.tick(60)
        #tick atualiza a tela a 60 frames por segundo
        tela.fill(cor_branca)
        #Preencho a tela com a cor branca
        tela.blit(sup, [0,0])
        #o comando blit adiciona a superfície

        # Colocar a posição do retângulo no mouse e
        # Colisões

        (xant, yant) = (ret.left, ret.top)  # Captura posiçãp do objeto antes da colisão
        (ret.left, ret.top) = pygame.mouse.get_pos()  # define a posição do retângulo no mouse
        ret.left -= ret.width / 2  # Define o centro do retângulo como o centro de sua largura (posição do mouse)
        ret.top -= ret.width / 2  # Define o centro objeto no cento de sua altura


        #if ret.colliderect(ret2):  # Se houver colisão com outro objeto
            #ret2.inflate_ip(3,3)
            #Animação para inflar o retângulo

            #text = fonte_perdeu.render('COLIDIU',1,cor_verde)
            #tela.blit(text, [150,400])
            #audio_explosao.play()

            #(ret.left, ret.top) = (xant, yant)  # define a posição do objeto para a posição anterior a colisão

        # Comandos para criar e exbir contador
        segundos = pygame.time.get_ticks()/1000
        #Armazeno o tempo de execução do prgrama em milisegundos

        segundos = str(segundos)
        #Coverto a informação em uma STring
        contador = fonte_texto.render(segundos,0,cor_branca)
        #"Renderiza" o contador para ser mostrado na tela
        tela.blit(contador,(300,10))
        #adiciona o contador a tela


        pygame.draw.rect(tela, cor_vermelha, ret)#Desenha retangulo
        pygame.draw.rect(tela, cor_azul, ret2)  # Desenha retangulo
        pygame.display.update()#Atualizações da tela

    pygame.quit()#Fecha a janela

main()
