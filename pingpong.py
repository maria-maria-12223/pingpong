from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, widht, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (widht, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed() 
        if keys[K_UP]  and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys[K_DOWN]  and self.rect.y < 400:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed() 
        if keys[K_w]  and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys[K_s]  and self.rect.y < 400:
            self.rect.y += self.speed

speed = 20
speed_x = 3
speed_y = 3
win_h = 700
win_w = 500
FPS = 60
clock = time.Clock()
font.init()
font2 = font.Font(None, 75)
display.set_caption('Пинг Понг')
window = display.set_mode((700, 500))
window.fill((135, 206, 235))
ball = GameSprite('arbyz.png', 330, 230 , 8, 65, 65)
player_1 = Player('pupsen.png', 20, 200, 10, 100, 110)
player_2 = Player('vupsen.png', 550, 200, 10, 100, 110)
win = font2.render('VUPSEN IS WIN!', True, (255, 215, 0))
loser = font2.render('PUPSEN IS WIN!', True, (255, 0, 0))
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill((135, 206, 235))
        player_1.update_l()  
        player_1.reset() 
        player_2.update_r()  
        player_2.reset()
        ball.reset()
        ball.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
                speed_x *= -1

        if ball.rect.y < 0 or ball.rect.y > 450:
            speed_y *= -1

        if ball.rect.x < 0 and not finish:
            finish = True
            window.blit(win,(135, 200))
        if ball.rect.x > 650 and not finish:
            finish = True
            window.blit(loser,(135, 200))

    display.update()
    clock.tick(FPS)
