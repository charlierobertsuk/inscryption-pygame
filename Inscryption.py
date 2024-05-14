import pygame, random, os
from PIL import Image
import pillow_avif

pygame.init()

cards = {
    # Talking cards
    "BulletAnt": {"health":1, "attack":1, "blood":1, "bones":0}, 
    "PineMarten": {"health":2, "attack":1, "blood":1, "bones":0}, 
    "BrianCoral": {"health":4, "attack":0, "blood":0, "bones":4}, # Says: "Hi, I'm Brian"
    
    # Ground cards
    "Hamster": {"health":1, "attack":0, "blood":0, "bones":0}, # Starter card
    "Mole": {"health":1, "attack":0, "blood":0, "bones":0}, # Alternative starter card, moves to block if nothing to block
    
    "Deer": {"health":3, "attack":2, "blood":0, "bones":3},
    "BlackMamba": {"health":1, "attack":2, "blood":0, "bones":4}, # Kills cards instantly
    "HoppingMouse": {"health":1, "attack":1, "blood":0, "bones":1},
    "Armadillo": {"health":4, "attack":1, "blood":3, "bones":0}, # Reflects 1 of incoming damage
    "Opossum": {"health":1, "attack":1, "blood":1, "bones":0},  
    "SlowLoris": {"health":1, "attack":3, "blood":2, "bones":0}, # 1 venom damage to opponent for 3 turns
    "Wolverine": {"health":2, "attack":2, "blood":2, "bones":0},
    "Hedgehog": {"health":1, "attack":1, "blood":1, "bones":0},
    "Tapir": {"health":3, "attack":1, "blood":2, "bones":0},
    "Rhino": {"health":6, "attack":2, "blood":4, "bones":0},
    "Anteater": {"health":2, "attack":1, "blood":1, "bones":0},
    "Capybara": {"health":2, "attack":1, "blood":1, "bones":0},
    "PolarBear": {"health":4, "attack":4, "blood":4, "bones":0},
    "Monkey": {"health":3, "attack":2, "blood":3, "bones":0},
    
    # Water cards
    "Seal": {"health":3, "attack":1, "blood":2, "bones":0},
    "GoblinShark": {"health":2, "attack":2, "blood":2, "bones":0},
    "FlyingFish": {"health":1, "attack":1, "blood":1, "bones":0},
    "Tuna": {"health":2, "attack":1, "blood":2, "bones":0},
    "BlobFish": {"health":4, "attack":0, "blood":3, "bones":0},
    "MimicOctopus": {"health":0, "attack":0, "blood":2, "bones":0}, # Mirrors opponent attack and health 
    "Axolotl": {"health":1, "attack":1, "blood":1, "bones":0},
    "Narwhal": {"health":3, "attack":3, "blood":3, "bones":0},
    "Platypus": {"health":2, "attack":2, "blood":2, "bones":0},
    "PerryThePlatypus": {"health":10, "attack":5, "blood":6, "bones":0}, # Legendary "evolution"
    
    # Air cards
    "Moorhen": {"health":2, "attack":1, "blood":1, "bones":0},
    "Shoebill": {"health":1, "attack":2, "blood":0, "bones":3},
    "Pigeon": {"health":1, "attack":1, "blood":1, "bones":0},
    "Falcon": {"health":2, "attack":3, "blood":2, "bones":0},
    "BaldEagle": {"health":3, "attack":3, "blood":3, "bones":0},
    "RunnerDuck": {"health":1, "attack":1, "blood":1, "bones":0},
    "Buzzard": {"health":3, "attack":2, "blood":3, "bones":0}, # Dodges first attack when played, 20% dodge chance
    "RoadRunner": {"health":1, "attack":2, "blood":2, "bones":0}, # 10% dodge chance
    "Vulture": {"health":3, "attack":2, "blood":0, "bones":0} # 5% chance to appear in hand when something dies
}

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Inscryption")

card_image = pygame.image.load("inscryptioncard.jpg")

def draw_card(card, x, y):
    card_image = pygame.transform.scale(pygame.image.load("inscryptioncard.jpg"), (100, 150))
    screen.blit(card_image, (x, y))
    
    animal_image_path = f"{card.lower()}.jpg" 
    if not os.path.exists(animal_image_path):
        animal_image_path = f"{card.lower()}.png"
    if not os.path.exists(animal_image_path):
        animal_image_path = f"{card.lower()}.jfif"
    if not os.path.exists(animal_image_path):
        animal_image_path = f"{card.lower()}.webp"
    
    try:
        animal_image = pygame.image.load(animal_image_path)
    except pygame.error:
        animal_image = pygame.Surface((80, 80))
        animal_image.fill((255, 0, 0))
    
    animal_image = pygame.transform.scale(animal_image, (70, 70)) 

    animal_x = x + (card_image.get_width() - animal_image.get_width()) // 2
    animal_y = y + (card_image.get_height() - animal_image.get_height()) // 2 - 10

    screen.blit(animal_image, (animal_x, animal_y))

    font = pygame.font.Font(None, 18)

    red = (255, 0, 0)
    green= (0, 255, 0)
    blue = (0, 0, 255)
    blood = (178, 0, 0)
    bones = (135, 103, 16)
    health = (225, 90, 184)
    attack = (0, 0, 0)

    text_x = x + 10
    text_y = y + 10
    draw_text(str(cards[card]["health"]), font, health, screen, text_x + 72, text_y + 120)
    draw_text(str(cards[card]["attack"]), font, attack, screen, text_x + 2, text_y + 105)
    draw_text(str(cards[card]["blood"]), font, blood, screen, text_x + 72, text_y)
    draw_text(str(cards[card]["bones"]), font, bones, screen, text_x + 2, text_y)

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
