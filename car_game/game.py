from time import sleep
from pygame import *
import random
from random import randint, choice

wn = display.set_mode((1000, 600))
display.set_caption("Race")

fon = transform.scale(image.load("road.png"), (1000, 600))
play_again_img = transform.scale(image.load("play_again.png"), (250, 100))  
start_game_img = transform.scale(image.load("start_game.png"), (400, 200))  
exit_game_img = transform.scale(image.load("exit_game.png"), (275, 150))    
you_win_img = transform.scale(image.load("you_win.png"), (250,100))
game_over_img = transform.scale(image.load("game_over.png"), (250,200))
game = 1
clock = time.Clock()

mixer.init()
mixer.music.load("race_music.ogg")
mixer.music.play()
crash_sound = mixer.Sound("crash_sound.ogg")
font.init()
font1 = font.Font(None, 50)
font2 = font.Font(None, 50)
font3 = font.Font(None, 50)
font4 = font.Font(None,60)

lose = 0
catch = 0

label_lose = font1.render(f"Пропущено {lose}", True, (193, 17, 11))
label_catch = font1.render(f"Збито {catch}", True, (13, 197, 11))
label_win = font3.render("Кінець гри!", True, (193, 17, 11))
label_winning = font2.render("ПеРЕмОгА", True, (13, 197, 11))

class Player(sprite.Sprite):
    def __init__(self, image_player, x, y, size_x, size_y, life, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_player), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.life = life

    def show(self):
        wn.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 337:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 600:
            self.rect.x += self.speed

random_x = [354, 462, 571]

class Enemy(Player):
    def update(self):
        global lose
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = -10
            self.rect.x = random.choice(random_x)
            self.speed = 5
            lose += 1

car_main = Player("car_red.png", 500, 470, 70, 100, 3, 3)

car_y = sprite.Group()
for i in range(1):
    enemy = Enemy("car_yellow.png", random.choice([354, 462, 571]), 0, 50, 100, randint(1, 5), randint(1, 5))
    car_y.add(enemy)

car_w = sprite.Group()
for i in range(1):
    cars = Enemy("car_white.png", random.choice([354, 462, 571]), 0, 50, 100, randint(1, 5), randint(1, 5))
    car_w.add(cars)

lose_game = 0
finish = 0

def reset_game():
    global lose, catch, finish, lose_game
    lose = 0
    catch = 0
    finish = 0
    lose_game = 0
    car_main.rect.x = 500
    car_main.rect.y = 470
    for enemy in car_y:
        enemy.rect.y = -10
        enemy.rect.x = random.choice(random_x)
        enemy.speed = randint(3, 8)
    for car in car_w:
        car.rect.y = -10
        car.rect.x = random.choice(random_x)
        car.speed = randint(3, 8)

# Відображення стартового екрану
def show_start_screen():
    wn.blit(fon, (0, 0))
    wn.blit(start_game_img, (300, 100))  # Відображаємо картинку "start_game.png" посередині екрану
    wn.blit(exit_game_img, (350, 350))  # Відображаємо картинку "exit_game.png" під кнопкою "start_game.png"
    display.update()
    waiting = True
    while waiting:
        for e in event.get():
            if e.type == QUIT:
                return False
            if e.type == MOUSEBUTTONDOWN and e.button == 1:  # Перевіряємо клік мишею
                x, y = e.pos
                # Перевіряємо, чи клік був у межах зображення кнопки "start_game.png"
                if 300 <= x <= 700 and 100 <= y <= 300:
                    return True
                # Перевіряємо, чи клік був у межах зображення кнопки "exit_game.png"
                if 300 <= x <= 700 and 350 <= y <= 550:
                    return False
    return False

# Показуємо стартовий екран
if not show_start_screen():
    game = 0

while game:
    wn.blit(fon, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = 0
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            if finish and 400 <= x <= 600 and 250 <= y <= 350:  # Перевіряємо, чи натиснули на картинку "play_again.png"
                reset_game()

    car_y.draw(wn)
    car_w.draw(wn)

    label_lose = font1.render(f"Об'їжджати {lose}", True, (255, 255, 255))
    label_catch = font1.render(f"Ціль: {catch}", True, (255, 255, 255))
    if not finish:
        car_y.update()
        car_w.update()

        if sprite.spritecollide(car_main, car_y, False):
            label_win = font3.render("Кінець гри!", True, (193, 17, 11))
            wn.blit(label_win, (10, 80))
            crash_sound.play()
            finish = 1
            lose_game = 1

        if sprite.spritecollide(car_main, car_w, False):
            label_win = font3.render("Кінець гри!", True, (193, 17, 11))
            wn.blit(label_win, (10, 80))
            crash_sound.play()
            finish = 1
            lose_game = 1
        car_main.move()

    if lose == 1:
        label_winning = font4.render("Перемога", True, (1,1,1))
        wn.blit(you_win_img, (395, 100))
        
        finish = 1

    if lose_game == 1:
      wn.blit(game_over_img, (395,100))

    if finish:
        wn.blit(play_again_img, (400, 250))  # Відображаємо картинку "play_again.png"

    wn.blit(label_catch, (10, 10))
    wn.blit(label_lose, (10, 45))

    car_main.show()
    clock.tick(120)
    display.update()