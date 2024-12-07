from pygame import *
wn = display.set_mode((600,600))
display.set_caption("Лабіринт")

fon = transform.scale(image.load("background.jpg"),(600,600))
FPS = 120
game = 1
clock = time.Clock()

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
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
hero = Player("hero.png",100,140,100,100,3,3)
enemy = Player("cyborg.png",450,400,100,100,3,1)
finish = Player("treasure.png",300,200,80,50,0,0)
while game:
    wn.blit(fon,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = 0
    hero.show()
    enemy.show()
    finish.show()
    hero.move()
    clock.tick(FPS)
    display.update()