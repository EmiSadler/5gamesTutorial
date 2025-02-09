import pygame
from os.path import join
from random import randint

# General set up
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True

# plain surface
surf = pygame.Surface((100,200))
surf.fill('aquamarine4')
x = 100
y = 150

# surface stars
star_surface = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(20)]

# importing an image to surface
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# import a meteor
meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# import laser
laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #  draw the game
    display_surface.fill('black')
    for pos in star_positions:
        display_surface.blit(star_surface, pos)
    if player_rect.right < WINDOW_WIDTH:
        player_rect.left += 0.2
    elif player_rect.left > WINDOW_WIDTH:
        player_rect.right += 0.2
    display_surface.blit(player_surf, player_rect)
    display_surface.blit(meteor_surf, meteor_rect)
    pygame.display.update()


pygame.quit()