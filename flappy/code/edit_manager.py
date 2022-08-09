import pygame
from settings import *
from os import walk


class SurfaceManager:
    """
    - #!import graphics,
    - #!resize for the surface,
    - #!add color to blocks based on remaining health
    - return to the Game()
    """

    def __init__(self):
        for index, info in enumerate(walk("flappy/assets/blocks")):
            for image_name in info[2]:
                pass

    def get_surface(self, block_type, size):
        image = pygame.Surface(size)
        image.fill("green")
        return image
