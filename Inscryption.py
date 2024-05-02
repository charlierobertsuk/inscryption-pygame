import pygame, sys, cards

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

# constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (204, 145, 92)

# variables
cardsize = 100
card = pygame.Rect((screen_width//2-cardsize//2), (screen_height//2+50), cardsize, cardsize*1.7)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # background colour
    screen.fill(WHITE) 
    
    # draw
    pygame.draw.rect(screen, BROWN, card)

    # display update
    pygame.display.flip()

    # set game fps
    clock.tick(60)
