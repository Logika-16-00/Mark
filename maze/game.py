from time import sleep
from pygame import *
import pygame
wn = display.set_mode((1000,600))
display.set_caption("Лабіринт")

fon = transform.scale(image.load("background.jpg"),(1000,600))
FPS = 120
game = 1
dx= 2
clock = time.Clock()

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

font.init()
font1 = font.Font(None, 70)
font2 = font.Font(None, 20)

win = font1.render("You win", True, (23,231,43))
lose = font1.render("You lose", True, (250,87, 9))
money = mixer.Sound("money.ogg")

kick = mixer.Sound("kick.ogg")
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

class Wall(sprite.Sprite):
    def __init__(self, color,x,y,size_x,size_y):
        super().__init__()
        self.color = color
        self.size_x = size_x
        self.size_y = size_y
        self.wall = Surface((self.size_x, self.size_y))
        self.wall.fill(self.color) 
        self.rect = self.wall.get_rect()
        self.rect.x = x
        self.rect.y = y
    def wall_draw(self):
        wn.blit(self.wall, (self.rect.x, self.rect.y))

color = (32,54,122)
wall1 = Wall(color,0,0,1000,10)
wall2 = Wall(color,0,600-10,1000,10)
wall3 = Wall(color,0,0,10,600)
wall4 = Wall(color,1000-10,0,10,600)

wall_maze1 = Wall(color,200,150,10,500)
wall_maze2 = Wall(color,400,10,10,300)
wall_maze3 = Wall(color,400,300,150,10)
wall_maze4 = Wall(color,700,150,10,500)
wall_maze5 = Wall(color,850,10,10,300)

life1 = Player("live.png",10,0,50,50,3,3) 
life2 = Player("live.png",75,0,50,50,3,3)
life3 = Player("live.png",130,0,50,50,3,3)                 
hero = Player("hero.png",50,475,100,100,3,3)
enemy = Player("cyborg.png",900,325,100,100,3,1)
finish = Player("treasure.png",900,50,80,50,0,0)
while game:
    wn.blit(fon,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = 0
    hero.show()
    enemy.show()
    finish.show()
    hero.move()
    wall1.wall_draw()
    wall2.wall_draw()
    wall3.wall_draw()
    wall4.wall_draw()
    wall_maze1.wall_draw()
    wall_maze2.wall_draw()
    wall_maze4.wall_draw()
    wall_maze3.wall_draw()
    wall_maze5.wall_draw()
    life1.show()
    life2.show()
    life3.show()
    walls = [wall1, wall2, wall3, wall4, wall_maze5, wall_maze1,wall_maze3, wall_maze2, wall_maze4]
    if sprite.collide_rect(hero,enemy):
        kick.play()
        wn.blit(lose,(400,200))
        hero.rect.x = 50
        hero.rect.y = 475
        # game = 0
    if sprite.collide_rect(hero,finish):
        money.play()
        wn.blit(win,(400,200))
        # game = 0  
    for wall in walls:
        if sprite.collide_rect(hero,wall):
         wn.blit(lose,(400,200))
         hero.rect.x = 50
         hero.rect.y = 475

    enemy.rect.x += dx

    if enemy.rect.x > 1000 or enemy.rect.x < 700:
        dx *= -1
    clock.tick(FPS)
    display.update()