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
        self.old_rect = self.rect.copy()
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
        # previous position temp
        self.old_rect = self.rect.copy()
        self.input()
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.screenstop()


class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, player, blocks):
        super().__init__(groups)

        # objects with collision
        self.player = player
        self.blocks = blocks
        # TODO : Redraw ball(again)
        self.image = pygame.image.load("flappy/assets/others/ball.gif").convert_alpha()

        # ball position
        self.rect = self.image.get_rect(midbottom=player.rect.midtop)
        self.old_rect = self.rect.copy()
        self.pos = pygame.math.Vector2(self.rect.topleft)

        # choise allows to change directions
        self.direction = pygame.math.Vector2((choice((1, -1)), -1))
        self.speed = 1.1
        # if active
        self.active = False

    def window_collision(self, direction):
        if direction == "horizontal":
            if self.rect.left < 0:
                self.rect.left = 0
                self.pos.x = self.rect.x
                self.direction.x *= -1
            elif self.rect.right > WINDOW_WIDTH:
                self.rect.right = WINDOW_WIDTH
                self.pos.x = self.rect.x
                self.direction.x *= -1
        elif direction == "vertical":
            if self.rect.top < 0:
                self.rect.top = 0
                self.pos.y = self.rect.y
                self.direction.y *= -1
            elif self.rect.bottom > WINDOW_HEIGHT:
                self.active = False
                self.direction.y = -1

    def collision(self, direction):
        overlaping = pygame.sprite.spritecollide(self, self.blocks, False)
        if self.rect.colliderect(self.player.rect):
            overlaping.append(self.player)
        if overlaping:
            if direction == "horizontal":
                for sprite in overlaping:
                    if (
                        self.rect.right >= sprite.rect.left
                        and self.old_rect.right <= sprite.old_rect.left
                    ):
                        self.rect.right = sprite.rect.left - 1  # offset
                        self.pos.x = self.rect.x
                        self.direction.x *= -1

                    if (
                        self.rect.left <= sprite.rect.right
                        and self.old_rect.left >= sprite.old_rect.right
                    ):
                        self.rect.left = sprite.rect.right + 1  # offset
                        self.pos.x = self.rect.x
                        self.direction.x *= -1

                    if getattr(sprite, "health", None):
                        sprite.get_damage(1)

            elif direction == "vertical":
                for sprite in overlaping:
                    if (
                        self.rect.bottom >= sprite.rect.top
                        and self.old_rect.bottom <= sprite.old_rect.top
                    ):
                        self.rect.bottom = sprite.rect.top - 1  # offset
                        self.pos.y = self.rect.y
                        self.direction.y *= -1

                    if (
                        self.rect.top <= sprite.rect.bottom
                        and self.old_rect.top >= sprite.old_rect.bottom
                    ):
                        self.rect.top = sprite.rect.bottom + 1  # offset
                        self.pos.y = self.rect.y
                        self.direction.y *= -1

                    if getattr(sprite, "health", None):
                        sprite.get_damage(1)

    def update(self, dt):

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            # previous position temp
            self.old_rect = self.rect.copy()

        if self.active:
            self.pos.x += self.direction.x * self.speed * dt
            self.rect.x = round(self.pos.x)
            self.collision("horizontal")
            self.window_collision("horizontal")
            # separation of the movement axis
            self.pos.y += self.direction.y * self.speed * dt
            self.rect.y = round(self.pos.y)
            self.collision("vertical")
            self.window_collision("vertical")
        else:
            self.rect.midbottom = self.player.rect.midtop
            self.pos = pygame.math.Vector2(self.rect.topleft)


class Block(pygame.sprite.Sprite):
    def __init__(self, block_type, pos, groups) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((BLOCK_WIDTH, BLOCK_HEIGHT))
        self.rect = self.image.get_rect(topleft=pos)
        self.old_rect = self.rect.copy()
        # damage calculation
        self.health = int(block_type)

    def get_damage(self, amount):
        self.health -= amount
        if self.health > 0:
            # update block
            pass
        else:
            self.kill()
