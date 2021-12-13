import pygame_menu
import source.game

def getMainMenu(screen_width, screen_height, menus):

    def framePreset(frame, widget):
        frame = frame.pack(widget,
                   align=pygame_menu.locals.ALIGN_CENTER,
                   vertical_position=pygame_menu.locals.POSITION_CENTER,
                   margin=(0,10)
                   )
        return frame

    def widgetPreset(widget):
        widget._background_color = (255, 165, 0)
        widget.set_border(1, (0, 0, 0))
        return widget

    scoreMenu = menus[0]
    shipMenu = menus[1]
    settingsMenu = menus[2]

    background_image = pygame_menu.BaseImage(
        image_path = "images/background.png",
        drawing_mode = pygame_menu.baseimage.IMAGE_MODE_FILL
    )

    # Make beauty here
    mytheme = pygame_menu.themes.THEME_DEFAULT.copy()
    mytheme.title_background_color = (0, 0, 0)
    mytheme.background_color = background_image
    mytheme.title_font = pygame_menu.font.FONT_FIRACODE_BOLD
    mytheme.widget_font = pygame_menu.font.FONT_OPEN_SANS_BOLD
    mytheme.widget_font_color = (0, 0, 0)

    menu = pygame_menu.Menu('SpaceExplorer', screen_width, screen_height, theme=mytheme)

    menu.add.menu_link(scoreMenu, "scoreMenu")
    menu.add.menu_link(shipMenu, "shipMenu")
    menu.add.menu_link(settingsMenu, "settingsMenu")

    framy = menu.add.frame_v(width=screen_width * 0.6, height=screen_height * 0.6,
                             background_color = (255, 165, 0, 100)
    )
    framePreset(framy, widgetPreset(menu.add.button('Играть', source.game.playGame, menu, screen_width, screen_height)))
    framePreset(framy, widgetPreset(menu.add.button('Личный рекорд', menu.get_widget("scoreMenu").open)))
    framePreset(framy, widgetPreset(menu.add.button('Выбрать корабль', menu.get_widget("shipMenu").open)))
    framePreset(framy, widgetPreset(menu.add.button('Настройки', menu.get_widget("settingsMenu").open)))
    framePreset(framy, widgetPreset(menu.add.button('Выход', pygame_menu.events.EXIT)))


    return menu
