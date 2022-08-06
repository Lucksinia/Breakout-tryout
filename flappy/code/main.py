import pygame, sys
from settings import *
from sprites import Player


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Breakout!")
        self.clock = pygame.time.Clock()
        self.bg = self.create_bg()
        # groops(sprites)
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self.all_sprites)

    def create_bg(self):  # Scale up bg by calculating scale factor
        bg_original = pygame.image.load("flappy/assets/others/bg.png").convert()
        scale_factor = WINDOW_HEIGHT / bg_original.get_height()
        scaled_height = bg_original.get_height() * scale_factor
        scaled_width = bg_original.get_width() * scale_factor
        scaled_bg = pygame.transform.scale(bg_original, (scaled_width, scaled_height))
        return scaled_bg

    def run(self, DT=60):
        while True:
            dt = self.clock.tick(60)  # delta time
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.all_sprites.update(dt)  # update the game internally
            self.display_surface.blit(self.bg, (0, 0))
            self.all_sprites.draw(self.display_surface)

            pygame.display.update()  # update the whole surface


if __name__ == "__main__":
    game = Game()
    game.run(DT)
