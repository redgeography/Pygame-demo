import pygame
from threading import thread
from time import sleep
from pyautogui import size

pygame.init()
class Speed:
  def __init__(speed, accel, accel_rate, terminal_velocity, decel_rate = accel_rate * 2):
    
