from pygame import *
from random import randint

# Música de fondo
mixer.init()
mixer.music.load('fire.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

# Necesitamos las siguientes imágenes:
img_back = "galaxy.jpg" # Fondo de juego
img_hero = "rocket.png" # Héroe
img_bullet = "bullet.png" # Bala
img_enemy = "ufo.png" # Enemigo

score = 0
goal = 10
lost = 0
max_lost

class Player(GameSprite):
    def update(self):
        kays = kay.get_pressed()
        if kays(K_LEFT) and self.rect.x > 5:
            self.rect.x -= self.speed
        if kays(K_RIGHT) and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        Bullet = bullet(img_bullet, self.rect.centex, self.rect.top, 15, 20, -15)
        Bullet.add(bullet)