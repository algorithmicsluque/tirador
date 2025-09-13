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

# Clase padre para otros objetos
class GameSprite(sprite.Sprite):
    # Constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Llamamos al constructor de la clase (Sprite):
        sprite.Sprite.__init__(self)

        # Cada objeto debe almacenar una propiedad image
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # Cada objeto debe almacenar la propiedad rect en la cual está inscrito
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # Método que dibuja al personaje en la ventana
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Clase de jugador principal
class Player(GameSprite):
   # Método para controlar el objeto con las teclas de las flechas
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
           
class Enemy(GameSprite):
   # Método para mover al enemigo
   def update(self):
       self.rect.y += self.speed
       global lost
       if self.rect.y > win_height:
              self.rect.x = randint(80, win_width - 80)
              self.rect.y = 0
              lost = lost + 1

    # Método para “disparar” (usa la posición del jugador para crear una bala)
   def fire(self):
       bullet = GameSprite(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
       return bullet

# Crea una ventana
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# Crea objetos
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)

monsters = sprite.Group()
for i in range(1,6):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1,5))
    monsters.add(monster)

# La variable “el juego terminó”: cuando sea True, los objetos dejan de funcionar en el ciclo principal
finish = False

# Ciclo de juego principal:
run = True # La bandera se restablece por el botón de cerrar ventana

while run:
   # Evento de pulsado del botón “Cerrar”
    for e in event.get():
       if e.type == QUIT:
           run = False
    if not finish:
       window.blit(background,(0,0))
       ship.update()
       ship.reset()
       display.update()
    time.delay(50)