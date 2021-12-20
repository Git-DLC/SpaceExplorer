import pygame_menu
import pickle

def getShipMenu(screen_width, screen_height):

    shipFile = "images/playerShip1_blue.png"
    def changeShip(value, ship):
        global shipFile
        shipFile = ship
        im = menu.get_widget("image")
        im.set_image(pygame_menu.baseimage.BaseImage(shipFile))

    def framePreset(frame, widget):
        frame = frame.pack(widget,
                           align=pygame_menu.locals.ALIGN_CENTER,
                           vertical_position=pygame_menu.locals.POSITION_CENTER,
                           margin=(0, 10)
                           )
        return frame

    def widgetPreset(widget):
        widget._background_color = (255, 165, 0)
        widget.set_border(1, (0, 0, 0))
        return widget

    def saveShip():
        global shipFile
        with open('settings.txt', 'rb') as file:
            settings = pickle.load(file)
        file.close()
        settings[2] = shipFile
        with open('settings.txt', 'wb') as file:
            pickle.dump(settings, file)
        file.close()

    background_image = pygame_menu.BaseImage(
        image_path="images/background.png",
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL
    )

    # Make beauty here
    mytheme = pygame_menu.themes.THEME_DEFAULT.copy()
    mytheme.title_background_color = (0, 0, 0)
    mytheme.background_color = background_image
    mytheme.title_font = pygame_menu.font.FONT_FIRACODE_BOLD
    mytheme.widget_font = pygame_menu.font.FONT_OPEN_SANS_BOLD
    mytheme.widget_font_color = (0, 0, 0)

    menu = pygame_menu.Menu('Выбрать корабль', screen_width, screen_height, theme=mytheme)

    framy = menu.add.frame_v(width=screen_width * 0.6, height=screen_height * 0.6,
                             background_color=(255, 165, 0, 100)
                             )

    framePreset(framy, widgetPreset(menu.add.image(shipFile, scale=(1, 1), image_id="image" ) ))
    framePreset(framy, widgetPreset(menu.add.selector(
        'Корабль :',
        [('Blue', "images/playerShip1_blue.png"),
         ('Red', "images/playerShip2_red.png")],
        onchange=changeShip
    )))
    framePreset(framy, widgetPreset(menu.add.button('Сохранить', saveShip)))
    framePreset(framy, widgetPreset(menu.add.button('Назад', pygame_menu.events.BACK)))

    return menu
