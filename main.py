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
max_lost = 3


class Enemy(GameSprite):
    def udapte(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_heihgt:
            self.rect.x = randint(80,win_widht - 80)
            self.rect.y = 0 
            lost = lost + 1