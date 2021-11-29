import pygame_menu

def getMainMenu(screen_width, screen_height, menus):
    scoreMenu = menus[0]
    shipMenu = menus[1]
    settingsMenu = menus[2]

    menu = pygame_menu.Menu('SpaceExplorer', screen_width, screen_height)

    menu.add.menu_link(scoreMenu, "scoreMenu")
    menu.add.menu_link(shipMenu, "shipMenu")
    menu.add.menu_link(settingsMenu, "settingsMenu")

    menu.add.button('Играть')
    menu.add.button('Личный рекорд', menu.get_widget("scoreMenu").open)
    menu.add.button('Выбрать корабль', menu.get_widget("shipMenu").open)
    menu.add.button('Настройки', menu.get_widget("settingsMenu").open)
    menu.add.button('Выход', pygame_menu.events.EXIT)

    return menu
