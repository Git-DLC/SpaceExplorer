import pygame_menu
import pickle

def getScoreMenu(screen_width, screen_height):
    menu = pygame_menu.Menu('Личный рекорд', screen_width, screen_height)

    #TEST?
    table = []

    with open('scores.txt', 'wb') as file:
        pickle.dump(table, file)


    table = menu.add.table(table_id='my_table', font_size=20)

    table.default_cell_padding = 5
    table.default_row_background_color = 'white'

    table.add_row(['Время', 'Дата', 'Очки'],
                  cell_font=pygame_menu.font.FONT_OPEN_SANS_BOLD)

    with open('scores.txt', 'rb') as file:
        settings = pickle.load(file)

    table.add_row(['A', 'B', 1])
    table.add_row(['α', 'β', 'γ'], cell_align=pygame_menu.locals.ALIGN_CENTER)

    menu.add.button('Назад', pygame_menu.events.BACK)

    return menu
