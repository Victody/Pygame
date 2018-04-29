import pygame

class Player(pygame.sprite.Sprite): #Classe con strutora do objeto jogador
    def __init__(self, imagem): #Funnção que converte uma imagem no objeto jogador
        self.imagem = imagem #Declaramos uma variável que representará a imagem a ser manipulada
        self.rect = self.imagem.get_rect() #Definimos o retangulo de colisão da imagem
        self.rect.left, self.rect.top = (240,250)#Posição inicial do Objeto

    def mover(self, vX, vY):
        self.rect.move_ip(vX, vY)

    def update(self, superficie):#Atualização de da imagem em cada frame
        superficie.blit(self.imagem, self.rect)#Adiciona a imagem a tela a cada atualização
