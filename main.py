import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font('UltimatePygameIntro/font/Pixeltype.ttf', 50) #*(font type, font size)
text_surface = test_font.render("My game", False, 'Black')

snail_surface = pygame.image.load('UltimatePygameIntro/graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 700

player_surface = pygame.image.load('UltimatePygameIntro/graphics/Player/player_stand.png').convert_alpha()
player_rectangle = player_surface.get_rect(topleft = (0, 225))

sky_surface = pygame.image.load('UltimatePygameIntro/graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('UltimatePygameIntro/graphics/ground.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (300, 50))
    snail_x_pos -= 3
    if snail_x_pos < -50: snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 275))
    player_rectangle.left += 1
    screen.blit(player_surface, player_rectangle)
    
    pygame.display.update()
    clock.tick(60)