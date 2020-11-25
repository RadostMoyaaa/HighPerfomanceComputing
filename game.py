import pygame,sys, random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
game_scr = pygame.display.set_mode((300, 300))

player_srf = pygame.Surface((20, 20))
player_rect = player_srf.get_rect(center=(300//2, 300//2))
player_spd_x = random.randint(1,3)
player_spd_y = random.randint(1,3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    game_scr.fill(WHITE)
    
    player_rect.centerx += player_spd_x
    player_rect.centery += player_spd_y
    
    if player_rect.top <= 0 or player_rect.bottom >= 300:
        player_spd_y *= -1
    
    if player_rect.left <= 0 or player_rect.right >= 300:
        player_spd_x *= -1
        
    game_scr.blit(player_srf, player_rect)
    
    pygame.display.update()
    pygame.time.delay(16)