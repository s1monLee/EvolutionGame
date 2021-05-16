import pygame
import random as rd

WIDTH = 50
HEIGHT = 50
MARGIN = 1
BOT_SIZE = 20

POPULATION_SIZE = 50

GAME_COLORS = {
    "border": (121, 121, 134),
    "empty_square": (255, 236, 179),
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "red": (255, 0, 0)
}


class GameSell:

    def __init__(self):
        self.is_bot = False
        self.color = GAME_COLORS["empty_square"]
        self.genome = [rd.randint(0, 3) for _ in range(64)]
        self.index = 0
        self.position = []
        self.energy = 99

    def get_genome_value(self) -> int:
        self.index += 1
        if self.index == 64:
            self.index = 0
        return self.genome[self.index]

    def set_energy(self):
        self.energy -= 1
        if self.energy == 0:
            self.is_bot = False


pygame.init()
pygame.font.init()
GAME_FONT = pygame.font.SysFont("Consolas", 15)

# Set the HEIGHT and WIDTH of the screen
display = pygame.display.set_mode(((MARGIN + BOT_SIZE) * WIDTH + MARGIN, (MARGIN + BOT_SIZE) * HEIGHT + MARGIN))

pygame.display.update()
pygame.display.set_caption("Evolution Game")

grid = [[GameSell() for _ in range(HEIGHT)] for _ in range(WIDTH)]

for bot in range(POPULATION_SIZE):
    x, y = rd.randint(0, WIDTH - 1), rd.randint(0, HEIGHT - 1)
    grid[x][y].is_bot = True
    grid[x][y].color = GAME_COLORS["green"]

clock = pygame.time.Clock()
running = True

while running:
    # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if grid[x][y].is_bot:
                if grid[x][y].get_genome_value() == 0 and x + 1 < WIDTH and not grid[x+1][y].is_bot:
                    grid[x][y].set_energy()
                    grid[x+1][y], grid[x][y] = grid[x][y], grid[x+1][y]
                elif grid[x][y].get_genome_value() == 1 and x - 1 > 0 and not grid[x-1][y].is_bot:
                    grid[x][y].set_energy()
                    grid[x-1][y], grid[x][y] = grid[x][y], grid[x-1][y]
                elif grid[x][y].get_genome_value() == 2 and y + 1 < HEIGHT and not grid[x][y+1].is_bot:
                    grid[x][y].set_energy()
                    grid[x][y+1], grid[x][y] = grid[x][y], grid[x][y+1]
                elif grid[x][y].get_genome_value() == 3 and y - 1 > 0 and not grid[x][y-1].is_bot:
                    grid[x][y].set_energy()
                    grid[x][y-1], grid[x][y] = grid[x][y], grid[x][y-1]

    display.fill(GAME_COLORS["border"])
    for i, row in enumerate(grid):
        for j, sell in enumerate(row):
            pygame.draw.rect(display,
                             sell.color,
                             [(MARGIN + BOT_SIZE) * i + MARGIN,
                              (MARGIN + BOT_SIZE) * j + MARGIN,
                              BOT_SIZE,
                              BOT_SIZE])
            if sell.is_bot:
                text_surface = GAME_FONT.render(str(sell.energy), False, (0, 0, 0))
                display.blit(text_surface,
                             [(MARGIN + BOT_SIZE) * i + MARGIN,
                              (MARGIN + BOT_SIZE) * j + MARGIN])
    pygame.display.update()
    # set FPS
    clock.tick(5)

# close game
pygame.quit()
quit()
