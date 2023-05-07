from pygame import *
from random import randint
font.init()
font1 = font.SysFont('Arial', 70)
font2 = font.SysFont('Arial', 20)
#__________________________________________________________________________________________________________________________________
bul = sprite.Group()

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-pong")
bg = transform.scale(image.load("bg.png"), (win_width, win_height))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.natural_speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.player_y = player_y
        self.width = width
        self.height = height
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update2(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x < win_heght - 80:
            self.rect.y += self.speed
    def update1(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.x < win_heght - 80:
            self.rect.y += self.speed
"""class Ball(GameSprite):
    pass
"""
"""racketka1 = Player('', 0, 0, 5, 20, 80)
racketka2 = Player('', win_width - 20, 0, 5, 20, 80)"""
game = True
clock = time.Clock()
FPS = 120
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(bg, (0, 0))

    display.update()  
    clock.tick(FPS)
