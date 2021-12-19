import pygame_menu
import pickle

def getScoreMenu(screen_width, screen_height):

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

    menu = pygame_menu.Menu('Личный рекорд', screen_width, screen_height, theme=mytheme)

    #TEST?
    table = []

    with open('scores.txt', 'wb') as file:
        pickle.dump(table, file)

    framy = menu.add.frame_v(width=screen_width * 0.6, height=screen_height * 0.6,
                             background_color=(255, 165, 0, 100)
                             )

    table = framePreset(framy, menu.add.table(table_id='my_table', font_size=20))

    table.default_cell_padding = 5
    table.default_row_background_color = 'white'

    table.add_row(['Время', 'Дата', 'Очки'],
                  cell_font=pygame_menu.font.FONT_OPEN_SANS_BOLD)

    with open('scores.txt', 'rb') as file:
        settings = pickle.load(file)
    
    values = []
    r = open('records.txt', 'r', encoding = "utf-8").read()      
    r = r.split(",")
    print(r)            

    table.add_row([r[0], r[1], r[2]])
    table.add_row([r[3], r[1], r[2]], cell_align=pygame_menu.locals.ALIGN_CENTER)

    framePreset(framy, widgetPreset(menu.add.button('Назад', pygame_menu.events.BACK)))

    return menu
