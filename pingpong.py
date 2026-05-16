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
win_h = 700
win_w = 500
FPS = 60
clock = time.Clock()
display.set_caption('Пинг Понг')
window = display.set_mode((700, 500))
window.fill((135, 206, 235))
player_1 = Player('pupsen.png', 20, 200, 20, 100, 110)
player_2 = Player('vupsen.png', 550, 200, 20, 100, 110)
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

    display.update()
    clock.tick(FPS)
