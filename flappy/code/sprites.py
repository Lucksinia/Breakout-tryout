import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        # basic setup(change later to actual png)
        self.image = pygame.Surface((WINDOW_WIDTH // 10, WINDOW_HEIGHT // 20))
        self.image.fill('red')

        #position on screen
        self.rect = self.image.get_rect(midbottom=(WINDOW_WIDTH // 2,WINDOW_HEIGHT - 20))
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.speed = 0.9
        

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def screenstop(self):
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
            self.pos.x = self.rect.x
        if self.rect.left < 0:
            self.rect.left = 0
            self.pos.x = self.rect.x
    
    def update(self, dt):
        self.input()
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.screenstop()

class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, player):
        super().__init__(groups)

        # !basic ball setup Don't work yet
        # TODO: Images that needed to load.
        self.image = pygame.image.load()