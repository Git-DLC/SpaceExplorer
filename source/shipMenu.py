import pygame_menu

def getShipMenu(screen_width, screen_height):
    menu = pygame_menu.Menu('Выбрать корабль', screen_width, screen_height)
    menu.add.selector('Корабль :', [('Корабль1', 1), ('Корабль2', 2)])
    menu.add.button('Назад', pygame_menu.events.BACK)

    return menu
