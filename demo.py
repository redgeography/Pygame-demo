import pygame
from pyautogui import size
from functools import reduce
from time import sleep
from random import randint
from math import floor

pygame.init()

rainbow_hue = 0

rainbow = pygame.Color(0, 0, 0)

calibri = pygame.font.SysFont("calibri", 55)

score = -1 # on the first call it gets pushed to 0



def random_dim(size):
    if randint(0, 1):
        return randint(0, floor(size * 0.4))
    else:
        return randint(floor(size * 0.6), size)


accel_dict = {
              "left": 20,
              "right": 20,
              "up": 20,
              "down": 20
              }

resolution = size()
surface = pygame.display.set_mode(resolution)
pygame.display.set_caption("square game :)")

# hitboxes
player_rect = pygame.Rect(0, 0, 50, 50)
target_rect = pygame.Rect(0, 0, 90, 90)
surf_rect = surface.get_rect()


keys = None
clock = pygame.time.Clock()




def key_pressed(*names):
    return reduce(lambda acc, x: acc or keys[getattr(pygame, "K_" + x)],names, False)


def reset():
    global score, rainbow_hue # apparently I have to do this
    player_rect.center = surf_rect.center
    target_rect.left = random_dim(resolution.width)
    target_rect.top = random_dim(resolution.height)
    target_rect.clamp_ip(surf_rect)
    score += 1
    rainbow_hue = 0
    accel_dict.update(
        {"left": 20,
         "right": 20,
         "up": 20,
         "down": 20,
         }
        )
    

def key_pressed(*names):
  return reduce(lambda acc, x: acc or keys[getattr(pygame, "K_" + x)],names, False)

should_break = False

reset()
while True:
    for x in pygame.event.get():
        if x.type is pygame.QUIT:
            pygame.quit()
            should_break = True



    if should_break:
        break


    if player_rect.colliderect(target_rect):
        reset()

    
    surface.fill("white")
    rainbow_hue += 2
    rainbow_hue %= 360
    rainbow.hsva = (rainbow_hue, 60, 100, 100)
    
    pygame.draw.rect(surface, "black", player_rect)
    pygame.draw.ellipse(surface, rainbow, target_rect)
    surface.blit(
        calibri.render("score: " + str(score), True, "black"), (0, 0)
        )

    
    keys = pygame.key.get_pressed()
    if key_pressed("a", "LEFT"):
        accel_dict["left"] = min(accel_dict["left"] + 1, 50) 
        player_rect.left -= accel_dict["left"]
    else:
        accel_dict["left"] = 20

    
    if key_pressed("w", "UP"):
        accel_dict["up"] = min(accel_dict["up"] + 1, 50) 
        player_rect.top -= accel_dict["up"]
    else:
        accel_dict["up"] = 20

    
    if key_pressed("d", "RIGHT"):
        accel_dict["right"] = min(accel_dict["right"] + 1, 50) 
        player_rect.right += accel_dict["right"]
    else:
        accel_dict["right"] = 20

    
    if key_pressed("s", "DOWN"):
        accel_dict["down"] = min(accel_dict["down"] + 1, 50)
        player_rect.bottom += accel_dict["down"]
    else:
        accel_dict["down"] = 20

    player_rect.clamp_ip(surf_rect)
    pygame.display.flip()
    clock.tick(60)


    
        
