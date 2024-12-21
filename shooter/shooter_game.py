#Створи власний Шутер!

from pygame import *
from random import *

wn =  display.set_mode((700,500))
display.set_caption("Shooter")

fon = transform.scale(image.load("galaxy.jpg"),(700,500))
finish = False
fps = 60
clock = time.Clock()


mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()



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


class Enemy(Player):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = -10




rocket = Player("rocket.png",310,360,  60,130,5,5)
monsters = sprite.Group()
for i in range(5):
    enemy = Enemy("ufo.png", randint(0,650), 0,90,60,randint(1,5),0)
    monsters.add(enemy)
game = 1
while game:
    for e in event.get():
        if e.type == QUIT:
            game = 0
    if not finish:
        wn.blit(fon,(0,0))
        rocket.show()
        rocket.move()
        monsters.draw(wn)

    display.update()
    clock.tick(fps)

