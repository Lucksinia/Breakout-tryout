from asyncio import events
import pygame, sys
from settings import *
from sprites import Player, Ball, Block


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Breakout!")
        self.clock = pygame.time.Clock()
        self.bg = self.create_bg()
        # groops(sprites)
        self.all_sprites = pygame.sprite.Group()
        self.block_sprites = pygame.sprite.Group()
        self.player = Player(self.all_sprites)
        self.stage_setup()
        self.ball = Ball(self.all_sprites, self.player, self.block_sprites)

    def create_bg(self):  # Scale up bg by calculating scale factor
        bg_original = pygame.image.load("flappy/assets/others/bg.png").convert()
        scale_factor = WINDOW_HEIGHT / bg_original.get_height()
        scaled_height = bg_original.get_height() * scale_factor
        scaled_width = bg_original.get_width() * scale_factor
        scaled_bg = pygame.transform.scale(bg_original, (scaled_width, scaled_height))
        return scaled_bg

    def stage_setup(self):
        """cycle thorought all rows and columns find positions of blocks"""
        for row_index, row in enumerate(BLOCK_MAP):
            for col_index, col in enumerate(row):
                if col != " ":
                    x = col_index * (BLOCK_WIDTH + GAP_SIZE) + GAP_SIZE // 2
                    y = row_index * (BLOCK_HEIGHT + GAP_SIZE) + GAP_SIZE // 2
                    Block(col, (x, y), [self.all_sprites, self.block_sprites])

    def run(self, DT=60):
        while True:
            dt = self.clock.tick(60)  # delta time
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ball.active = True

            self.all_sprites.update(dt)  # update the game internally
            self.display_surface.blit(self.bg, (0, 0))
            self.all_sprites.draw(self.display_surface)

            pygame.display.update()  # update the whole surface


if __name__ == "__main__":
    game = Game()
    game.run(DT)
