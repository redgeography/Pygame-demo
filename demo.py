import pygame
from pyautogui import size
from functools import reduce
from time import sleep
pygame.init()
surface = pygame.display.set_mode(size())
surf_rect = surface.get_rect()
keys = None
clock = pygame.time.Clock()
def key_pressed(*names):
    return reduce(lambda acc, x: acc or keys[getattr(pygame, "K_" + x)],names, False)
player_rect = pygame.Rect(0, 0, 50, 50)
player_rect.center = surf_rect.center

def initialize():
  def key_pressed(*names):
      return reduce(lambda acc, x: acc or keys[getattr(pygame, "K_" + x)],names, False)
  while True:
      for x in pygame.event.get():
          if x.type is pygame.QUIT:
              pygame.quit()
              return
      surface.fill("white")
      pygame.draw.rect(surface, "red", player_rect)
      keys = pygame.key.get_pressed()
      if key_pressed("a", "LEFT") and player_rect.left > 9:
          player_rect.left -= 10
      if key_pressed("w", "UP") and player_rect.top > 9:
          player_rect.top -= 10
      if key_pressed("d", "RIGHT") and surf_rect.right - player_rect.right > 9:
          player_rect.right += 10
      if key_pressed("s", "DOWN") and surf_rect.bottom - player_rect.bottom > 9:
          player_rect.bottom += 10
      pygame.display.flip()
      clock.tick(60)

initialize()
    
        
