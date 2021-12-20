# База основного окна
import pygame
import pygame_menu
import random
import os
import source.mainMenu
import source.scoreMenu
import source.settingMenu
import source.shipMenu
import source.game

# Настройки окна
screen_width = 800
screen_height = 600
FPS = 60

# Инициализация игры
pygame.init()

# Окно по центру экрана
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Размер окна и FPS
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

#dialogue_font = pygame.font.SysFont('arial', 15)
#dialogue = dialogue_font.render("Hey there, Beautiful weather today!", True, (0,0,0))
#

scoreMenu = source.scoreMenu.getScoreMenu(screen_width, screen_height)
shipMenu = source.shipMenu.getShipMenu(screen_width, screen_height)
settingsMenu = source.settingMenu.getSettingsMenu(screen_width, screen_height)
mainMenu = source.mainMenu.getMainMenu(screen_width, screen_height, [scoreMenu, shipMenu, settingsMenu])


mainMenu.mainloop(screen)

while True:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if mainMenu.is_enabled():
        mainMenu.update(events)
        mainMenu.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)