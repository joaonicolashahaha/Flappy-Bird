import pygame
import random

WIDTH = 1280
HEIGHT = 900

# create an obstucle 
def criar_cano():
    altura = random.randint(150, 700)
    gap = 200
    return {
        "x": WIDTH,
        "top": altura,
        "bottom": altura + gap
    }

#after death screen. TODO: study about this function
def tela_game_over():
    while True:
        screen.blit(bg_img, (0, 0))
        texto = font.render("Game Over!", True, (255, 255, 255))
        rect = texto.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(texto, rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.display.flip()
                    canos = [criar_cano()]
                    player_x = 200
                    player_y = 300
                    velocity = 0
                    running = True
                    return canos, player_y, player_x, velocity, running
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit
                    running = False
                    canos = [criar_cano()]
                    player_x = 200
                    player_y = 300
                    velocity = 0
                    return canos, player_y, player_x, velocity, running
                    
# start pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 48)
pygame.display.set_caption("Flappy Bird")

# set clock
clock = pygame.time.Clock()

# load background
bg_img = pygame.image.load("background.png").convert()
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

# load player
player_img = pygame.image.load("personagem.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (60, 60))

# player variables: TODO make a player class.
player_x = 200
player_y = 300
velocity = 0
gravity = 0.5

canos = [criar_cano()]

# set running as True
running = True

# using running to create the main game loop
while running:

    # check for pygame events
    for event in pygame.event.get():
        # if event == quit simply quit
        if event.type == pygame.QUIT:
            running = False
        # if event is key down:
        if event.type == pygame.KEYDOWN:
            # if event == keydown space:
            if event.key == pygame.K_SPACE:
                velocity = -10
    # isaac newton bro gravity is a variable lol
    velocity += gravity
    player_y += velocity

    player_rect = pygame.Rect(player_x, player_y, 60, 60)

    if player_y > HEIGHT or player_y < 0:
        canos, player_y, player_x, velocity, running = tela_game_over()
        print("Game Over")

    for cano in canos:
        cano["x"] -= 6

    if canos[-1]["x"] < WIDTH - 600:
        canos.append(criar_cano())

    if canos[0]["x"] < -60:
        canos.pop(0)

    screen.blit(bg_img, (0, 0))

    screen.blit(player_img, (player_x, player_y))

    for cano in canos:
        top_rect = pygame.Rect(cano["x"], 0, 60, cano["top"])
        bottom_rect = pygame.Rect(cano["x"], cano["bottom"], 60, HEIGHT)

        pygame.draw.rect(screen, (0, 255, 0), top_rect)
        pygame.draw.rect(screen, (0, 255, 0), bottom_rect)

        if player_rect.colliderect(top_rect) or player_rect.colliderect(bottom_rect):
            canos, player_y, player_x, velocity, running = tela_game_over()

    pygame.display.flip()
    clock.tick(60)

pygame.quit() 