import pygame, random

class Recs(object):
    def __init__(self, numInit):
        self.list = []
        for x in range(numInit):
            leftRandom = random.randrange(2,560)
            topRandom = random.randrange(-580, -10)
            width = random.randrange(10,30)
            heigth = random.randrange(15 , 30)
            self.list.append(pygame.Rect(leftRandom, topRandom, width, heigth))

    def RecsMove(self):
        for rect in self.list:
            rect.move_ip(0, 2)

    def cor(self, superficie):
        for rect in self.list:
            pygame.draw.rect(superficie,(165,214,254), rect)

    def ReDraw(self):
        for x in range(len(self.list)):
            if self.list[x].top > 481:
               leftRandom = random.randrange(2,560)
               topRandom = random.randrange(-580, -10)
               width = random.randrange(10,30)
               heigth = random.randrange(15 , 30)
               self.list[x] = (pygame.Rect(leftRandom, topRandom, width, heigth))
