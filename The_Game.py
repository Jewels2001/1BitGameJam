import pygame
import sys

import pygame_menu
from time import sleep
from pygame_menu import themes

################
# PYGAME SETUP
################
pygame.init()
screen = pygame.display.set_mode((1280, 720)) # menu tutorial calls screen
# surface = pygame.display.set_mode((600, 400))

background = pygame.Surface((1280, 720))
surface = pygame.Surface((10, 10))
surface.fill((0,255,0))

pos = [175, 125]

clock = pygame.time.Clock()
running = True

while running:
    ## PROCESSING
    
    ## EVENTS
    # poll/check for events
    # pygame.QUIT event means user clicked X to close window
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pos[0] += 20
    screen.fill("orange")
    #screen.blit(background, (0, 0))
    screen.blit(surface, pos)
    
    ## RENDERING
    # fill screen with a color to wipe last frame
    # screen.fill("orange")
    
    # if mainmenu.is_enabled():
    #     mainmenu.update(events)
    #     mainmenu.draw(screen)
    #     if (mainmenu.get_current().get_selected_widget()):
    #           arrow.draw(screen, mainmenu.get_current().get_selected_widget())
    
    # RENDER GAME HERE
    
    # flip() the display to put your work on the screen
    pygame.display.flip()
    # pygame.display.update()
    
    clock.tick(60) #limit FPS to 60
    
pygame.quit()
