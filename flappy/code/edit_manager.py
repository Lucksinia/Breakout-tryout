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
        self.sheet = pygame.image.load(
            "flappy/assets/blocks/blocks.png"
        ).convert_alpha()
        self.assets = {}
        for health, color in COLOR_LEGEND.items():
            self.assets[color] = health

    def get_surface(self, block_type, size):
        # return to the game
        image = pygame.Surface(size)
        # corners
        image.blit(self.sheet, (0, 0), (0, 0, 16, 16))  # topleft
        image.blit(self.sheet, ((size[0] - 16), 0), (32, 0, 16, 16))  # topright
        # top
        placeholder = image.blit(
            self.sheet, (0, 0), (16, 0, 16, 16)
        )  # TODO: re-do all of this
        # top
        top_width = size[0] - 32
        scaled_surf = pygame.Surface((placeholder.w, placeholder.h))
        scaled_top = pygame.transform.scale(
            scaled_surf, (top_width, scaled_surf.get_height())
        )

        image.blit(scaled_top, (scaled_top.get_width(), 0), (16, 0, 16, 16))  # top
        image.set_colorkey("BLACK")
        return image
