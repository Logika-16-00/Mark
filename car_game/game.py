from time import sleep
from pygame import *
import pygame
wn = display.set_mode((1000,600))
display.set_caption("Race")

fon = transform.scale(image.load("road.png"),(1000,600))
FPS = 120
game = 1
clock = time.Clock()


mixer.init()
mixer.music.load("race_music.ogg")
mixer.music.play()

font.init()
font1 = font.Font(None, 70)
font2 = font.Font(None, 20)

class Player(sprite.Sprite):
    def __init__(self, image_player,x,y,size_x,size_y,life,speed):
        super().__init__()
        self.image = transform.scale(image.load(image_player), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.life = life

    def show(self):
            wn.blit(self.image,(self.rect.x,self.rect.y))



    def move(self):
            keys = key.get_pressed()
            if keys[K_a]:
                self.rect.x -= self.speed
            if keys[K_d]:
                self.rect.x += self.speed

car_main = Player("car_red.png",500,470,100,100,3,3)
while game:
    wn.blit(fon,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = 0
    car_main.show()
    car_main.move()
    clock.tick(FPS)
    display.update()