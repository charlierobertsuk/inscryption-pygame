import cards, pygame, sys, random, time
from network import Network

# screen size
screen_width = 1000
screen_height = 500
half_width = screen_width // 2
half_height = screen_height // 2
screen = pygame.display.set_mode((screen_width, screen_height))

clientnumber = 0

# title
pygame.display.set_caption("Inscryption")

# clock
clock = pygame.time.Clock()

# initiate pygame
pygame.init()

# font
font = pygame.font.Font(None, 36)

print(cards.hampter["health"])

# constants
KYLE = ("#987654")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# variables
lives = 2

class Player():
    def __init__(self, x, y, screen_width, screen_height, colour):
        self.x = x
        self.y = y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.colour = colour
        self.rect = (x, y, screen_width, screen_height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            pass #NOTE: before server go to 12:48 to do client so position tracking works
        if keys[pygame.K_RIGHT]:
            pass
        if keys[pygame.K_UP]:
            pass
        if keys[pygame.K_DOWN]:
            pass


n = Network()
startPos = n.getPos()
# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # background colour
    screen.fill(KYLE) 

    
    # display update
    pygame.display.update()

    # set game fps
    clock.tick(60)