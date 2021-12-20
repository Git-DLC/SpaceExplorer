import pygame_menu
import pickle
import os.path


def getSettingsMenu(screen_width, screen_height):

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

    def saveFile():
        with open('settings.txt', 'rb') as file:
            settings = pickle.load(file)
        file.close()
        settings = [menu.get_widget('brightness').get_value(),
                    menu.get_widget('sound').get_value(),
                    settings[2]]
        with open('settings.txt', 'wb') as file:
            pickle.dump(settings, file)
        file.close()

    def loadFile():
        settings = [50, 50, "images/playerShip1_blue.png"]
        with open('settings.txt', 'rb') as file:
            settings = pickle.load(file)
        return settings

    settings = loadFile()

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

    menu = pygame_menu.Menu('Настройки', screen_width, screen_height, theme=mytheme)

    framy = menu.add.frame_v(width=screen_width * 0.6, height=screen_height * 0.6,
                             background_color=(255, 165, 0, 100)
                             )

    framePreset(framy, widgetPreset(menu.add.range_slider('Яркость', settings[0], (0, 100), 1,
                          rangeslider_id='brightness',
                          value_format=lambda x: str(int(x)))))
    framePreset(framy, widgetPreset(menu.add.range_slider('Звук', settings[1], (0, 100), 1,
                          rangeslider_id='sound',
                          value_format=lambda x: str(int(x)))))
    framePreset(framy, widgetPreset(menu.add.button('Сохранить', saveFile)))
    framePreset(framy, widgetPreset(menu.add.button('Назад', pygame_menu.events.BACK)))

    return menu
