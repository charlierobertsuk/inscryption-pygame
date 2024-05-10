import pygame, sys, random, cards

# screen size
screen_width = 1200
screen_height = 700
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

    # write numbers on the card
    attack_text = font.render(str(cards.hamster["attack"]), True, BLACK)
    defense_text = font.render(str(cards.hamster["health"]), True, BLACK)
    blood_text = font.render(str(cards.hamster["blood"]), True, BLACK)
    bones_text = font.render(str(cards.hamster["bones"]), True, BLACK)
    name_text = font.render(str("hamster"), True, BLACK)

    attack_text_rect = attack_text.get_rect(midbottom=(card.centerx + 30, card.bottom - 5))
    defense_text_rect = defense_text.get_rect(midbottom=(card.centerx - 30, card.bottom - 5))
    blood_text_rect = blood_text.get_rect(midtop=(card.centerx + 30, card.top + 5))
    bones_text_rect = bones_text.get_rect(midtop=(card.centerx - 30, card.top + 5))
    name_text_rect = name_text.get_rect(midtop=(card.centerx, card.top + (cardsize//2)*1.4))

    # display text
    screen.blit(attack_text, attack_text_rect)
    screen.blit(defense_text, defense_text_rect)
    screen.blit(blood_text, blood_text_rect)
    screen.blit(bones_text, bones_text_rect)
    screen.blit(name_text, name_text_rect)

    # display update
    pygame.display.flip()

    # set game fps
    clock.tick(60)