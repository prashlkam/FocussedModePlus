import pygame
import itertools

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FONT_SIZE = 28
BACKGROUND_COLOR = (0, 0, 0)  # Black
FOREGROUND_COLORS = [(255, 255, 255), (255, 255, 0), (173, 216, 230), (0, 255, 0)]  # White, Yellow, Light Blue, Green

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, FONT_SIZE)

# Read the key bindings from the file
with open('key_bindings.txt', 'r') as f:
    key_bindings = [line.split('|') for line in f.read().splitlines()]

# Create a color iterator
color_iterator = itertools.cycle(FOREGROUND_COLORS)

def draw_key_bindings():
    screen.fill(BACKGROUND_COLOR)
    for i, key_binding in enumerate(key_bindings):
        for j, column in enumerate(key_binding):
            text = font.render(column.strip(), True, next(color_iterator))
            if i >= 2:  # Draw a rectangle for the 3rd row and onwards
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(40 + j * 60, 40 + i * (FONT_SIZE + 10), 60, FONT_SIZE + 10), 1)         
            if j >= 2:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(40 + j * 60, 40 + i * (FONT_SIZE + 10), 500, FONT_SIZE + 10), 1)
            screen.blit(text, (50 + j * 60, 50 + i * (FONT_SIZE + 10)))
    pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_key_bindings()

pygame.quit()