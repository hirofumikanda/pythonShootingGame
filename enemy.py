import pygame as pg
import random

class Enemy():
    def __init__(self):
        x = random.randint(100, 500)
        y = -100
        self._image = pg.image.load("images/enemy1.png")
        self._rect = pg.Rect(x, y, 50, 50)
        self._vx = random.uniform(-4, 4)
        self._vy = random.uniform(1, 4)
        self._maxhp = 100
        self._hp = 100
        self._is_alive = True

    @property
    def is_alive(self):
        return self._is_alive
    @property
    def maxhp(self):
        return self._maxhp
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self, value):
        self._hp = value
    @property
    def rect(self):
        return self._rect
    @rect.setter
    def rect(self, value):
        self._rect = value
    @property
    def vy(self):
        return self._vy
    @vy.setter
    def vy(self, value):
        self._vy = value

    def update(self):
        if self._rect.x < 0 or self._rect.x > 550:
            self._vx = -self._vx
        self._rect.x += self._vx
        self._rect.y += self._vy
        if self._rect.y > 650:
            self._is_alive = False
    
    def draw(self, screen): # 描画処理
        screen.blit(self._image, self._rect)
        # hpbar
        rect1 = pg.Rect(self._rect.x, self._rect.y - 20, 4, 20)
        h = (self._hp / self._maxhp) * 20
        rect2 = pg.Rect(self._rect.x, self._rect.y - h, 4, h)
        pg.draw.rect(screen, pg.Color("RED"), rect1)
        pg.draw.rect(screen, pg.Color("GREEN"), rect2)

class FlameEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self._image = pg.image.load("images/enemy2.png")
        self._vx = random.uniform(-2, 2)
        self._vy = random.uniform(5, 7)

class IceEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self._image = pg.image.load("images/enemy3.png")
        self._maxhp = 150
        self._hp = 150

class BombEffect():
    def __init__(self, rect, effects):
        self._images = [
            pg.image.load("images/bomb_0.png"),
            pg.image.load("images/bomb_1.png"),
            pg.image.load("images/bomb_2.png"),
            pg.image.load("images/bomb_3.png"),
            pg.image.load("images/bomb_4.png"),
            pg.image.load("images/bomb_5.png")
        ]
        self._image = self._images[0]
        self._effects = effects
        self._rect = rect
        self._cnt = 0
    
    def update(self): # 更新処理
        self._cnt += 1
        idx = self._cnt
        if idx <= 5:
            self._image = self._images[idx]
        else:
            self._effects.remove(self)
    
    def draw(self, screen): # 描画処理
        screen.blit(self._image, self._rect)

class EnemyFactory():
    def create(self, etype): # タイプ指定で作る
        if etype == "flame":
            return FlameEnemy()
        if etype == "ice":
            return IceEnemy()
        return Enemy()
    
    def random_create(self): # ランダムに作る
        etype = random.choice(["normal", "flame", "ice"])
        return self.create(etype)