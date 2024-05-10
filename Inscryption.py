import pygame
import random

cards = {
    # Talking cards
    "bulletAnt": {"health":1, "attack":1, "blood":1, "bones":0}, 
    "pineMartin": {"health":2, "attack":1, "blood":1, "bones":0}, 
    "BrianCoral": {"health":4, "attack":0, "blood":0, "bones":4}, # Says: "Hi, I'm Brian"
    
    # Ground cards
    "hamster": {"health":1, "attack":0, "blood":0, "bones":0}, # Starter card
    "mole": {"health":1, "attack":0, "blood":0, "bones":0}, # Alternative starter card, moves to block if nothing to block
    
    "deer": {"health":3, "attack":2, "blood":0, "bones":3},
    "blackMamba": {"health":1, "attack":2, "blood":0, "bones":4}, # Kills cards instantly
    "hoppingMouse": {"health":1, "attack":1, "blood":0, "bones":1},
    "armadillo": {"health":4, "attack":1, "blood":3, "bones":0},
    "opossum": {"health":1, "attack":1, "blood":1, "bones":0},
    "slowLoris": {"health":1, "attack":3, "blood":2, "bones":0}, # Venom damage
    "wolverine": {"health":2, "attack":2, "blood":2, "bones":0},
    "hedgehog": {"health":1, "attack":1, "blood":1, "bones":0},
    "pinkFairyArmadillo": {"health":1, "attack":1, "blood":0, "bones":0}, # Dies if near water animal
    "beardedDragon": {"health":2, "attack":1, "blood":1, "bones":0},
    "tapir": {"health":3, "attack":1, "blood":2, "bones":0},
    "rhino": {"health":6, "attack":2, "blood":4, "bones":0},
    "anteater": {"health":2, "attack":1, "blood":1, "bones":0},
    "capybara": {"health":2, "attack":1, "blood":1, "bones":0},
    "polarBear": {"health":4, "attack":4, "blood":4, "bones":0},
    "proboscisMonkey": {"health":3, "attack":2, "blood":3, "bones":0},
    
    # Water cards
    "seal": {"health":3, "attack":1, "blood":2, "bones":0},
    "goblinShark": {"health":2, "attack":2, "blood":2, "bones":0},
    "flyingFish": {"health":1, "attack":1, "blood":1, "bones":0},
    "scorpionFish": {"health":1, "attack":2, "blood":2, "bones":0},
    "blobFish": {"health":4, "attack":0, "blood":3, "bones":0},
    "mimicOctopus": {"health":0, "attack":0, "blood":2, "bones":0}, # Mirrors opponent attack and health 
    "axolotl": {"health":1, "attack":1, "blood":1, "bones":0},
    "narwhal": {"health":3, "attack":3, "blood":3, "bones":0},
    "platypus": {"health":2, "attack":2, "blood":2, "bones":0},
    
    # Air cards
    "moorhen": {"health":2, "attack":1, "blood":1, "bones":0},
    "shoebill": {"health":1, "attack":2, "blood":0, "bones":3},
    "pigeon": {"health":1, "attack":1, "blood":1, "bones":0},
    "falcon": {"health":2, "attack":3, "blood":2, "bones":0},
    "baldEagle": {"health":3, "attack":3, "blood":3, "bones":0},
    "runnerDuck": {"health":1, "attack":1, "blood":1, "bones":0},
    "augurBuzzard": {"health":3, "attack":2, "blood":3, "bones":0}, # Dodges first attack when played, 20% dodge chance
    "roadRunner": {"health":1, "attack":2, "blood":2, "bones":0}, # 10% dodge chance
    "vulture": {"health":3, "attack":2, "blood":0, "bones":0} # 5% chance to appear in hand when something dies
}

pygame.init()

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Inscryption")

card_image = pygame.image.load("inscryptioncard.jpg")

def draw_card(card, x, y):
    card_image = pygame.transform.scale(pygame.image.load("inscryptioncard.jpg"), (100, 150))
    screen.blit(card_image, (x, y))
    font = pygame.font.Font(None, 24)
    text_color = (255, 255, 255)
    text_x = x + 10
    text_y = y + 10
    draw_text(card, font, text_color, screen, text_x, text_y)
    draw_text("Health: " + str(cards[card]["health"]), font, text_color, screen, text_x, text_y + 30)
    draw_text("Attack: " + str(cards[card]["attack"]), font, text_color, screen, text_x, text_y + 60)
    draw_text("Blood: " + str(cards[card]["blood"]), font, text_color, screen, text_x, text_y + 90)
    draw_text("Bones: " + str(cards[card]["bones"]), font, text_color, screen, text_x, text_y + 120)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def select_random_cards():
    card_names = list(cards.keys())
    return random.sample(card_names, 5)

def main():
    clock = pygame.time.Clock()
    FPS = 60
    running = True

    player_hand = select_random_cards()

    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for i, card_name in enumerate(player_hand):
            draw_card(card_name, 50 + i * 120, 400)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
