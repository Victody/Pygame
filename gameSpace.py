import pygame, PlayerClass, enemyRecs, time

def Collide(player, recs):
    for rec in recs.list:
        if player.rect.colliderect(rec):
            return True
    return False

def main():
    #Declarações de objetos
    pygame.init()

    screen_width = 480
    screen_heigth = 300
    tela = pygame.display.set_mode((screen_width,screen_heigth))

    onGame = True
    clock = pygame.time.Clock()

    img_nave = pygame.image.load('assets\imagem\F117Space.png').convert_alpha() #Carrego imagem para representar o player
    jogador = PlayerClass.Player(img_nave)#Inicializo o construtor da classe player

    enemy_rec = enemyRecs.Recs(30)

    img_explosion = pygame.image.load('assets\imagem\explosao.png').convert_alpha()

    rCollide = False

    img_bg = pygame.image.load('assets\imagem\Bg.png').convert_alpha()

    pygame.mixer.music.load('assets/audio/Steam snail - Steampunk fantasy music. Royalty free.mp3')
    pygame.mixer.music.play(loops = -1)


    som_explosion = pygame.mixer.Sound('assets/audio/399303__dogfishkid__explosion-012.ogg')
    som_move = pygame.mixer.Sound('assets/audio/tiroxpl.wav')

    vX, vY = 0, 0
    velocity = 10
    leftPress, rightPress, upPress, downPress = False, False, False, False

    cor_branca = (255, 255, 255)
    cor_preta = (5, 5, 5)
    cor_azul = (108, 194, 236)
    cor_verde = (54, 182, 112)
    cor_vermelha = (227, 57, 9)

    pygame.font.init()
    # Faz a pygame inicializar a classe de fontes

    fonte_perdeu = pygame.font.Font('assets/fonts/emulogic.ttf', 35)
    fonte_ganhou = pygame.font.Font('assets/fonts/emulogic.ttf', 12)

    while onGame:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                onGame = False

            if rCollide == False:
            #Movimento da nave pelo teclado
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        leftPress = True
                        vX = -velocity
                    if event.key == pygame.K_RIGHT:
                        rightPress = True
                        vX = velocity
                    if event.key == pygame.K_UP:
                        upPress = True
                        vY = -velocity
                    if event.key == pygame.K_DOWN:
                        downPress = True
                        vY = velocity
            if event.type == pygame.KEYUP:
                som_move.play()
                if event.key == pygame.K_LEFT: #Se a tecla direcional esquerda estiver levantado
                    leftPress = False #Declara Tecla esquerda não está pressionada
                    if rightPress: vX = velocity #Se o direcional direito estiver pressionado movimentar para a direita
                    else:vX = 0 #caso contrário não há tecla levantada
                if event.key == pygame.K_RIGHT:
                    rightPress = False
                    if leftPress: vX = -velocity
                    else:vX = 0
                if event.key == pygame.K_UP:
                    upPress = False
                    if downPress: vY = velocity
                    else:vY = 0
                if event.key == pygame.K_DOWN:
                    downPress = False
                    if upPress: vY = -velocity
                    else: vY = 0

        if Collide(jogador, enemy_rec):
            rCollide = True
            jogador.imagem = img_explosion
            pygame.mixer.music.stop()
            som_explosion.play()

        if rCollide == False:
            enemy_rec.RecsMove()
            jogador.mover(vX,vY)
            tela.blit(img_bg, (0, 0))
            seconds = pygame.time.get_ticks() / 1000
            seconds = str(seconds)
            cont_time = fonte_ganhou.render(seconds, 0, cor_branca)
            tela.blit(cont_time, (350, 10))

        clock.tick(27)

        enemy_rec.cor(tela)
        enemy_rec.ReDraw()
        jogador.update(tela)#Função update
        #jogador.mover(vX, vY)
        #enemy_rec.RecsMove()
        pygame.display.update()
    pygame.quit()

main()
