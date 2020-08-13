# ALL GAME OBJECTS
import pygame as pg
from settings import *
from random import uniform
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((32, 32))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = int(WIDTH / 2)
        self.rect.bottom = HEIGHT / 2
        self.speedx = 0
        self.last_shot = pg.time.get_ticks()

    def shoot(self):
        now = pg.time.get_ticks()
        if now - self.last_shot > 50:
            self.last_shot = now
            Bullet(self.game, (self.rect.centerx, self.rect.top))

    def get_keys(self):
        self.speedx = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.speedx = -5
        if keys[pg.K_RIGHT]:
            self.speedx = 5
        if keys[pg.K_SPACE]:
            self.shoot()

    def update(self):
        self.get_keys()
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


class Bullet(pg.sprite.Sprite):
    def __init__(self, game, pos):
        self.groups = game.all_sprites, game.bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.speedy = -10
        self.rect.centerx = self.pos.x

    def update(self):
        self.pos.y += self.speedy
        # delete the bullet if it goes off screen in y direction
        if self.pos.y < 0:
            self.kill()
