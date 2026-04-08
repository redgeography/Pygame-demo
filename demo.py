import pygame
from pyautogui import size
from functools import reduce
from time import sleep
pygame.init()
surface = pygame.display.set_mode(size())
surf_rect = surface.get_rect()
keys = pygame.key.get_pressed()
def key_pressed(*names):
    return reduce(lambda acc, x: acc or keys[getattr(pygame, "K_" + x)], False)
player_rect = pygame.Rect(0, 0, 50, 50)
while True:
    surface.fill("white")
    pygame.draw.rect(surface, "red", player_rect)
    if key_pressed("a", "LEFT") and player_rect.left > 9:
        player_rect.left -= 10
    elif key_pressed("w", "UP") and player_rect.top > 9:
        player_rect.top += 10
    elif key_pressed("d", "RIGHT") and surf_rect.right - player_rect.right > 9:
        player_rect.right += 10
    elif key_pressed("s", "DOWN") and surf_rect.bottom - player_rect.bottom > 9:
        player_rect.bottom += 10
    pygame.display.flip()
    sleep(1 / 60)
    
        
