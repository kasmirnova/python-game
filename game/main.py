import pygame
import sys
import random


class Aurora :
    def __init__(self) :
        self.screen = pygame.display.set_mode((400 , 708))
        self.aurora = pygame.Rect(65 , 50 , 50 , 50)
        self.background = pygame.image.load("sprites/background.png").convert()
        self.SubnauticaSprites = [pygame.image.load("sprites/first_v.png").convert_alpha() ,
                                  pygame.image.load("sprites/second_v.png").convert_alpha() ,
                                  pygame.image.load("sprites/dead.png")]
        self.columnUp = pygame.image.load("sprites/b_column.png").convert_alpha()
        self.columnDown = pygame.image.load("sprites/t_column.png").convert_alpha()
        self.gap = 135
        self.columnx = 400
        self.auroraY = 350
        self.jump = 0
        self.jumpSpeed = 10
        self.gravity = 5
        self.dead = False
        self.sprite = 0
        self.counter = 0
        self.offset = random.randint(-110 , 110)

    def updateColumnes(self) :
        self.columnx -= 2
        if self.columnx < -80 :
            self.columnx = 400
            self.counter += 1
            self.offset = random.randint(-110 , 110)

    def auroraUpdate(self) :
        if self.jump :
            self.jumpSpeed -= 1
            self.auroraY -= self.jumpSpeed
            self.jump -= 1
        else :
            self.auroraY += self.gravity
            self.gravity += 0.2
        self.aurora[1] = self.auroraY
        up_rect = pygame.Rect(self.columnx ,
                              360 + self.gap - self.offset + 10 ,
                              self.columnUp.get_width() - 10 ,
                              self.columnUp.get_height())
        down_rect = pygame.Rect(self.columnx ,
                               0 - self.gap - self.offset - 10 ,
                               self.columnDown.get_width() - 10 ,
                               self.columnDown.get_height())
        if up_rect.colliderect(self.aurora) :
            self.dead = True
        if down_rect.colliderect(self.aurora) :
            self.dead = True
        if not 0 < self.aurora[1] < 720 :
            self.aurora[1] = 50
            self.auroraY = 50
            self.dead = False
            self.counter = 0
            self.columnx = 400
            self.offset = random.randint(-110 , 110)
            self.gravity = 5

    def run(self) :
        clock = pygame.time.Clock()
        ###### фоновый музон
        pygame.init()
        pygame.mixer.music.load(f"sound/song.mp3")
        pygame.mixer.music.play(-1)
        ######
        pygame.font.init()

        font = pygame.font.SysFont("Arial" , 30)
        while True :
            clock.tick(60)
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    sys.exit()
                if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not self.dead :
                    self.jump = 17
                    self.gravity = 5
                    self.jumpSpeed = 10

            self.screen.fill((255 , 255 , 255))
            self.screen.blit(self.background , (0 , 0))
            self.screen.blit(self.columnUp ,
                             (self.columnx , 360 + self.gap - self.offset))
            self.screen.blit(self.columnDown ,
                             (self.columnx , 0 - self.gap - self.offset))
            self.screen.blit(font.render(str(self.counter) , -1 , (255 , 255 , 255)) , (200 , 50))
            if self.dead :
                self.sprite = 2
            elif self.jump :
                self.sprite = 1
            self.screen.blit(self.SubnauticaSprites[self.sprite] , (70 , self.auroraY))
            if not self.dead :
                self.sprite = 0
            self.updateColumnes()
            self.auroraUpdate()
            pygame.display.update()


if __name__ == "__main__" :
    Aurora().run()
