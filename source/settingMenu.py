import pygame_menu
import pickle
import os.path


def getSettingsMenu(screen_width, screen_height):

    def saveFile():
        settings = [menu.get_widget('brightness').get_value(),
                    menu.get_widget('sound').get_value()]
        with open('settings.txt', 'wb') as file:
            pickle.dump(settings, file)

    def loadFile():
        settings = [50, 50]
        with open('settings.txt', 'rb') as file:
            settings = pickle.load(file)
        return settings

    settings = loadFile()
    menu = pygame_menu.Menu('Настройки', screen_width, screen_height)
    menu.add.range_slider('Яркость', settings[0], (0, 100), 1,
                          rangeslider_id='brightness',
                          value_format=lambda x: str(int(x)))
    menu.add.range_slider('Звук', settings[1], (0, 100), 1,
                          rangeslider_id='sound',
                          value_format=lambda x: str(int(x)))
    menu.add.button('Сохранить', saveFile)
    menu.add.button('Назад', pygame_menu.events.EXIT)

    return menu
