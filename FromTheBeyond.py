# Importing pygame and other dependencies
import pygame

# Initiate pygame
pygame.init()

# Window management
pygame.display.set_mode((800, 600))
pygame.display.set_caption("From The Beyond")

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False