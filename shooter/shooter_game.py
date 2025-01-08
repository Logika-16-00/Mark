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
fire_sound = mixer.Sound("fire.ogg")
font.init()
font1 = font.Font(None,30)
font2 = font.Font(None,30)
lose =  0
catch = 0
label_lose = font1.render(f"Пропущено {lose}", True, (190,5,9))
label_catch = font1.render(f"Збито {lose}", True, (13,193,11))

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
    
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.x+15+7,self.rect.y,15,15,0,randint(8,15))
        bullets.add(bullet)

bullets = sprite.Group()


class Enemy(Player):
    def update(self):
        global lose
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = -10
            self.rect.x = randint(0,650)
            self.speed = randint(1,5)
            lose +=1
class Bullet(Player):
    def update(self):
        if self.rect.y < 0:
            self.kill()
        self.rect.y -= 5



rocket = Player("rocket.png",310,360,  60,130,5,5)
monsters = sprite.Group()
for i in range(5):
    enemy = Enemy("ufo.png", randint(0,650), 0,90,60,randint(1,5),randint(1,5))
    monsters.add(enemy)
game = 1
while game:
    for e in event.get():
        if e.type == QUIT:
            game = 0
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                rocket.fire()

    if not finish:
        label_lose = font1.render(f"Пропущено {lose}", True, (190,5,9))
        label_catch = font1.render(f"Збито {catch}", True, (13,193,11))
        wn.blit(fon,(0,0))
        rocket.show()
        rocket.move()
        monsters.draw(wn)
        monsters.update()
        bullets.draw(wn)
        bullets.update()
        wn.blit(label_catch, (10,10))
        wn.blit(label_lose, (10,45))

    display.update()
    clock.tick(fps)

