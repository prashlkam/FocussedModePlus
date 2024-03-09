import pygame
import itertools

class keybindings :
    def init(self):

        # Initialize Pygame
        pygame.init()

        # Set up some constants
        self.WIDTH, self.HEIGHT = 800, 600
        self.FONT_SIZE = 28
        self.BACKGROUND_COLOR = (0, 0, 0)  # Black
        self.FOREGROUND_COLORS = [(255, 255, 255), (255, 255, 0), (173, 216, 230), (0, 255, 0)]  # White, Yellow, Light Blue, Green

        # Create the window
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # Set up the font
        self.font = pygame.font.Font(None, self.FONT_SIZE)

        # Read the key bindings from the file
        with open('key_bindings.txt', 'r') as f:
            self.key_bindings = [line.split('|') for line in f.read().splitlines()]

        # Create a color iterator
        self.color_iterator = itertools.cycle(self.FOREGROUND_COLORS)

    def draw_key_bindings(self):
        self.screen.fill(self.BACKGROUND_COLOR)
        for i, key_binding in enumerate(self.key_bindings):
            for j, column in enumerate(key_binding):
                text = self.font.render(column.strip(), True, next(self.color_iterator))
                if i >= 2:  # Draw a rectangle for the 3rd row and onwards
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(40 + j * 60, 40 + i * (self.FONT_SIZE + 10), 60, self.FONT_SIZE + 10), 1)         
                if j >= 2:
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(40 + j * 60, 40 + i * (self.FONT_SIZE + 10), 500, self.FONT_SIZE + 10), 1)
                self.screen.blit(text, (50 + j * 60, 50 + i * (self.FONT_SIZE + 10)))
        pygame.display.flip()

# Main loop
if __name__ == '__main__':
    kbnd = keybindings()
    kbnd.init()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        kbnd.draw_key_bindings()

    pygame.quit()