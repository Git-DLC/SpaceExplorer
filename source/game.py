import pygame
import source.gameOverMenu
import random
from os import path
import datetime
import pickle
from datetime import date

def playGame(menu, screen_width, screen_height):
    img_dir = path.join(path.dirname(__file__), '../images')
    snd_dir = path.join(path.dirname(__file__), '../sound')

    menu.disable()
    menu.full_reset()

    gameOverMenu = source.gameOverMenu.getGameOverMenu(menu, screen_width, screen_height)

    with open('settings.txt', 'rb') as file:
        brightness, loudness, shipFile = pickle.load(file)
    WIDTH = screen_width
    HEIGHT = screen_height
    FPS = 60

    # Задаем цвета
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    # Создаем игру и окно
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SpaceExplorer!")
    clock = pygame.time.Clock()

    font_name = pygame.font.match_font('arial')


    def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)


    class Player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(player_img, (50, 38))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.radius = 20
            # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
            self.speedx = 0

        def update(self):
            self.speedx = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.speedx = -8
            if keystate[pygame.K_RIGHT]:
                self.speedx = 8
            self.speedy = 0
            if keystate[pygame.K_UP]: 
                self.speedy = -8
            if keystate[pygame.K_DOWN]: 
                self.speedy = 8
            self.rect.y += self.speedy
            self.rect.x += self.speedx
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.top > HEIGHT-40:
                self.rect.top = HEIGHT-40
            if self.rect.bottom < 40:
                self.rect.bottom = 40

        def shoot(self):
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            shoot_sound.play()

    class Mob1(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(bonys_img, (30, 40))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
            self.speedx = random.randrange(-3, 3)
    
        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(1, 8)
            
    class Mob(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image_orig = random.choice(meteor_images)
            self.image_orig.set_colorkey(BLACK)
            self.image = self.image_orig.copy()
            self.rect = self.image.get_rect()
            self.radius = int(self.rect.width * .85 / 2)
            # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-150, -100)
            self.speedy = random.randrange(1, 8)
            self.speedx = random.randrange(-3, 3)
            self.rot = 0
            self.rot_speed = random.randrange(-8, 8)
            self.last_update = pygame.time.get_ticks()

        def rotate(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > 50:
                self.last_update = now
                self.rot = (self.rot + self.rot_speed) % 360
                new_image = pygame.transform.rotate(self.image_orig, self.rot)
                old_center = self.rect.center
                self.image = new_image
                self.rect = self.image.get_rect()
                self.rect.center = old_center

        def update(self):
            self.rotate()
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(1, 8)

    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = bullet_img
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.centerx = x
            self.speedy = -10

        def update(self):
            self.rect.y += self.speedy
            # убить, если он заходит за верхнюю часть экрана
            if self.rect.bottom < 0:
                self.kill()


    # Загрузка всей игровой графики
    background = pygame.image.load(path.join(img_dir, "starfield.png")).convert()
    background_rect = background.get_rect()
    player_img = pygame.image.load(path.join(shipFile)).convert()
    player_img.set_colorkey((0, 0, 0, 255 - (brightness/100)*255))
    bonys_img = pygame.image.load(path.join(img_dir, "star_gold.png")).convert()
    bullet_img = pygame.image.load(path.join(img_dir, "laserRed01.png")).convert()
    meteor_images = []
    meteor_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png', 'meteorBrown_med1.png',
                   'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png',
                   'meteorBrown_tiny1.png']

    for img in meteor_list:
        meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())
    # Загрузка мелодий игры
    shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))
    expl_sounds = []
    for snd in ['expl3.wav', 'expl6.wav']:
        expl_sounds.append(pygame.mixer.Sound(path.join(snd_dir, snd)))
    pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
    pygame.mixer.music.set_volume(loudness)
    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    mobs1 = pygame.sprite.Group()
    #текущая дата
    current_date = date.today()
    ### надо бонус
    for i in range(2):
        m = Mob1()
        all_sprites.add(m)
        mobs1.add(m)
    
    for i in range(8):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    score = 0
    pygame.mixer.music.play(loops=-1)
    start_ticks=pygame.time.get_ticks()
    # Цикл игры
    running = True
    while running:
        # время
        seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds    

        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # проверка для закрытия окна
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # Обновление
        all_sprites.update()

        # проверка, попала ли пуля в моб
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            score += 50 - hit.radius
            random.choice(expl_sounds).play()
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)

        # Проверка, не ударил ли моб игрока
        hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
        if hits:
            # заносим очки в файл
            with open('records.txt','a', encoding = "utf-8") as out:
                out.write('{},{},{},'.format(seconds,current_date,score))       
            out.close()
            running = False
        
        # Проверка, не ударил ли моб игрока
        hits = pygame.sprite.spritecollide(player, mobs1, True)
        if hits:
            score += 60
            for hit in hits:
                m = Mob1()
                all_sprites.add(m)
                mobs1.add(m)
            running = True
        # Рендеринг
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, str(score), 18, 200, 10)
        draw_text(screen, str(seconds), 18, 600, 10)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.mixer.music.stop()
    gameOverMenu.mainloop(screen)

    menu.enable()
    menu.mainloop(screen)

