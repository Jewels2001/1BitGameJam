# main menu

import pygame

import pygame_menu
from time import sleep
from pygame_menu import themes
from screen import Screen
from button import Button

pygame.init()
pygame.font.init()
surface = pygame.display.set_mode((600, 400))

## multiple screens tutorial
menuScreen = Screen("Menu Screen")
control_bar = Screen("Control Screen")

win = menuScreen.makeCurrentScreen()

# MENU BUTTON
MENU_BUTTON = Button(150, 150, 150, 50, (255, 250, 250),
                     (255, 0, 0), "TimesNewRoman",
                     (255, 255, 255), "Main Menu")
 
# CONTROL BUTTON
CONTROL_BUTTON = Button(150, 150, 150, 50, (0, 0, 0),
                        (0, 0, 255), "TimesNewRoman",
                        (255, 255, 255), "Back")
 
done = False
 
toggle = False


## end tutorial code

def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)

def start_the_game():
    # mainmenu._open(loading)
    pass

def level_menu():
    mainmenu._open(level)



mainmenu = pygame_menu.Menu('Welcome', 600, 400,
                            theme=themes.THEME_SOLARIZED)
mainmenu.add.text_input('Name: ', default='username', maxchar=20)
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Levels', level_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

level = pygame_menu.Menu('Select a Difficulty', 600, 400,
                         theme=themes.THEME_BLUE)
level.add.selector('Difficulty:', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)

arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (10, 15))


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    ### multiple screens tutorial
    menuScreen.screenUpdate()
    control_bar.screenUpdate()
    
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    
    if menuScreen.checkUpdate((25, 0, 255)):
        control_barbutton = MENU_BUTTON.focusCheck(mouse_pos, mouse_click)
        
        MENU_BUTTON.showButton(menuScreen.returnTitle())
        if control_barbutton:
            win = control_bar.makeCurrentScreen()
            menuScreen.endCurrentScreen()
    elif control_bar.checkUpdate((255, 0, 255)):
        return_back = CONTROL_BUTTON.focusCheck(mouse_pos, mouse_click)
        
        CONTROL_BUTTON.showButton(control_bar.returnTitle())
        
        if return_back:
            control_bar.endCurrentScreen()
            win = menuScreen.makeCurrentScreen()
    
    pygame.display.update()
    
    ## end of multiple screens code

"""
    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)
        if (mainmenu.get_current().get_selected_widget()):
            arrow.draw(surface, mainmenu.get_current().get_selected_widget())
"""
   