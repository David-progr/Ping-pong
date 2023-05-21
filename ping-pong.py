from pygame import *
from random import randint
from time import sleep
font.init()
font1 = font.SysFont('Arial', 70)
font2 = font.SysFont('Arial', 20)
lose1 = font1.render('Player 1 lose!', True, (0, 0, 0))
lose2 = font1.render('Player 2 lose!', True, (0, 0, 0))
#__________________________________________________________________________________________________________________________________
bul = sprite.Group()
lose_ball1 = 0
lose_ball2 = 0
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
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 110:
            self.rect.y += self.speed
    def update1(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 110:
            self.rect.y += self.speed
play1 = Player('racket.png', 20, 0, 5, 20, 100)
play2 = Player('racket.png', win_width - 40, 0, 5, 20, 100)
ball = GameSprite('ball.png', win_width / 2, win_height / 2, 0, 40, 40)
game = True
clock = time.Clock()
FPS = 120
finish = False

speed_y = 2
speed_x = 2

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(bg, (0, 0))
        play1.update1()
        play2.update2()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(play1, ball) or sprite.collide_rect(play2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height - 40 or ball.rect.y <= 0:
            speed_y *= -1
        if ball.rect.x <= 0:
            lose_ball1 += 1
            ball.rect.x = 340
            ball.rect.y = 240
            sleep(1)
            speed_x *= -1
            speed_y *= 1
        if ball.rect.x >= win_width - 40:
            lose_ball2 += 1
            ball.rect.x = 340
            ball.rect.y = 240
            sleep(1)
            speed_x *= -1
            speed_y *= 1
        score1 = font2.render(f'Счет 1: {lose_ball2}', True, (0, 0, 0))
        window.blit(score1,(0, 0))
        score2 = font2.render(f'Счет 2: {lose_ball1}', True, (0, 0, 0))
        window.blit(score2,(0, 20))
        if lose_ball1 >= 5:
            window.blit(lose1, (200, 200))
            finish = True
        if lose_ball2 >= 5:
            window.blit(lose2, (200, 200))
            finish = True
    display.update()
    clock.tick(FPS)
