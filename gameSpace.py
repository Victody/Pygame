import pygame, PlayerClass, enemyRecs

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

    vX, vY = 0, 0
    velocity = 10
    leftPress, rightPress, upPress, downPress = False, False, False, False

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
        if rCollide == False:
            enemy_rec.RecsMove()
            jogador.mover(vX,vY)

        clock.tick(27)
        tela.blit(img_bg, (0, 0))
        enemy_rec.cor(tela)
        enemy_rec.ReDraw()
        jogador.update(tela)#Função update

        #jogador.mover(vX, vY)
        #enemy_rec.RecsMove()




        pygame.display.update()

    pygame.quit()

main()
