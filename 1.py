import pygame
import os
import sys


pygame.init()
clock = pygame.time.Clock()
size = width, height = 900, 700
screen = pygame.display.set_mode(size)

FPS = 50

# основной персонаж
player = None

buttons_start = pygame.sprite.Group()
play = pygame.sprite.Sprite()
info = pygame.sprite.Sprite()
buttons_start.add(play)
buttons_start.add(info)

player = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
stairs_group = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def generate_level(level):
    # реализация генерации уровня
    pass


class Player(pygame.sprite.Group):
    def __init__(self, pos_x, pos_y):
        super().__init__(player, all_sprites)
        self.image = None                      # сделать изображение героя
        self.rect = 0, 0                       # выбрать поожение героя
        self.pos = (pos_x, pos_y)

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move()
        # реализовать перемещение героя


class Buck(pygame.sprite.Group):
    pass


class Stairs(pygame.sprite.Sprite):
    stairs_image = load_image('stairs.png', pygame.Color('white'))

    def __init__(self, x, y):
        super().__init__(stairs_group, all_sprites)
        self.image = Stairs.stairs_image
        self.image = pygame.transform.scale(self.image, (30, 100))  # размер лестницы
        self.rect = self.image.get_rect().move(x, y)
        # self.rect.x = x
        # self.rect.y = y


class Platforms(pygame.sprite.Sprite):
    platform_image = load_image('platform.png', pygame.Color('white'))

    def __init__(self, x, y):
        super().__init__(platform_group, all_sprites)
        self.image = Platforms.platform_image
        self.image = pygame.transform.scale(self.image, (50, 30))  # размер платформы
        self.rect = self.image.get_rect().move(x, y)
        # self.rect.x = x
        # self.rect.y = y


class Monster(pygame.sprite.Group):
    pass


class Hammer(pygame.sprite.Group):
    pass


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    screen.fill((30, 30, 30))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN: # проверяем, если было нажатие на стартовом экране
                x, y = event.pos
                for box in buttons_start:
                    if box.rect.collidepoint(x, y):
                        pass  # решить вопрос с кнопками на стартовом меню
        pygame.display.flip()
        clock.tick(FPS)


start_screen()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # сделать реализацию движения героя с помощью стрелок
            if event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_DOWN:
                pass
            elif event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()
# завершение работы:
pygame.quit()