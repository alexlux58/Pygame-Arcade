import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font()

# test_surface = pygame.Surface((100,200))
# test_surface.fill('blue')

sky_surface = pygame.image.load('UltimatePygameIntro/graphics/Sky.png')
ground_surface = pygame.image.load('UltimatePygameIntro/graphics/ground.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    
    pygame.display.update()
    clock.tick(60)