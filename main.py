import pygame
import random as rd

WIDTH = 50
HEIGHT = 50
MARGIN = 2
BOT_SIZE = 20

colors = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "BLUE": (0, 0, 255),
    "GREED": (0, 255, 0),
    "RED": (255, 0, 0)
}


class bot:

    def __init__(self):
        self.genome = [rd.randint(0, 7)] * 64
        self.pos = [rd.randrange(0, WIDTH - 10, 10),
                    rd.randrange(0, HEIGHT - 10, 10),
                    10, 10]


pygame.init()
pygame.font.init()
GAME_FONT = pygame.font.SysFont("Consolas", 15)

# Set the HEIGHT and WIDTH of the screen
display = pygame.display.set_mode(((MARGIN + BOT_SIZE) * WIDTH + MARGIN, (MARGIN + BOT_SIZE) * HEIGHT + MARGIN))

pygame.display.update()
pygame.display.set_caption("Evolution Game")

grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
# population = [bot() for i in range(50)]

grid[3][2] = 1

running = True

while running:
    # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display.fill((121, 121, 134))

    for row in range(WIDTH):
        for column in range(HEIGHT):
            color = (255, 236, 179)
            if grid[row][column] == 1:
                color = colors["GREED"]
            pygame.draw.rect(display,
                             color,
                             [(MARGIN + BOT_SIZE) * column + MARGIN,
                              (MARGIN + BOT_SIZE) * row + MARGIN,
                              BOT_SIZE,
                              BOT_SIZE])
            if color == colors["GREED"]:
                text_surface = GAME_FONT.render("99", False, (0, 0, 0))
                display.blit(text_surface,
                             [(MARGIN + BOT_SIZE) * column + MARGIN,
                              (MARGIN + BOT_SIZE) * row + MARGIN])
    pygame.display.update()

# close game
pygame.quit()
quit()
