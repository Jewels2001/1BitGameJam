import pygame
from dataclasses import dataclass

@dataclass
class Screen():
    
    # Fill is screen colour, (0, 0, 255) is a color code
    def __init__(self, title, width=1280, height=720, fill=(0, 0, 255)):
        self.height = height
        self.title = title
        self.width = width
        self.fill = fill
        self.CurrentState = False
    
    # Choose current screen to display
    def makeCurrentScreen(self):
        pygame.display.set_caption(self.title)
        self.CurrentState = True
        self.screen = pygame.display.set_mode((self.width, self.height))
    
    # Turn off current screen
    def endCurrentScreen(self):
        self.CurrentState = False
        
    # Confirm screen changed
    def checkUpdate(self, fill):
        self.fill = fill
        return self.CurrentState
    
    # Update screen
    def screenUpdate(self):
        if self.CurrentState:
            self.screen.fill(self.fill)
        
    # Return title of current screen
    def returnTitle(self):
        return self.screen