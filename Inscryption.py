import cards, pygame, sys, random, time

# screen size
screen_width = 1000
screen_height = 500
half_width = screen_width // 2
half_height = screen_height // 2
screen = pygame.display.set_mode((screen_width, screen_height))

# title
pygame.display.set_caption("Inscryption")

# clock
clock = pygame.time.Clock()

# initiate pygame
pygame.init()

# font
font = pygame.font.Font(None, 36)

# state colours
KYLE = ("#987654")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

print(cards.hampter["health"])

# constants

# variables

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