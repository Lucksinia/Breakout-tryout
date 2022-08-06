import pygame
from settings import *
from random import choice


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        # basic setup(change later to actual png)
        self.image = pygame.Surface((WINDOW_WIDTH // 10, WINDOW_HEIGHT // 20))
        self.image.fill("red")

        # position on screen
        self.rect = self.image.get_rect(
            midbottom=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 20)
        )
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

        # objects with collision
        self.player = player
        # !basic ball setup Don't work yet
        self.image = pygame.image.load("flappy/assets/others/bg.png").convert_alpha()

        # ball position
        self.rect = self.image.get_rect(midbottom=player.rect.midtop)
        self.pos = pygame.math.Vector2(self.rect.topleft)

        # choise allows to change directions
        self.direction = pygame.math.Vector2((choice((1, -1)), -1))
        self.speed = 1.1
        # if active
        self.active = False

    def update(self, dt):
        if self.active:
            pass
        else:
            self.rect.midbottom = self.player.rect.midtop
            self.pos = pygame.math.Vector2(self.rect.topleft)
