import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll/check for events
    # pygame.QUIT event means user clicked X to close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # fill screen with a color to wipe last frame
    screen.fill("orange")
    
    # RENDER GAME HERE
    
    # flip() the display to put your work on the screen
    pygame.display.flip()
    
    clock.tick(60) #limit FPS to 60
    
pygame.quit()