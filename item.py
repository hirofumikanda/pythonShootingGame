import pygame as pg
import random

class Item():
    def __init__(self):
        x = random.randint(100, 500)
        y = -100
        self._image = pg.image.load("images/item1.png")
        self._rect = pg.Rect(x, y, 50, 50)
        self._vx = 0
        self._vy = random.uniform(1, 4)
        self._hpRecovery = 0
        self._is_existed = True
    
    @property
    def rect(self):
        return self._rect
    
    @property
    def is_existed(self):
        return self._is_existed
    
    @property
    def hpRecovery(self):
        return self._hpRecovery
    
    def update(self): # 更新処理
        self._rect.x += self._vx
        self._rect.y += self._vy
        if self._rect.y > 650:
            self._is_existed = False
    
    def draw(self, screen): # 描画処理
        screen.blit(self._image, self._rect)

class RecoveryItem(Item):
    def __init__(self):
        super().__init__()
        self._image = pg.image.load("images/item1.png")
        self._hpRecovery = 50

class ItemFactory():
    def create(self, itype): # タイプ指定で作る
        if itype == "recovery":
            return RecoveryItem()
        return Item()
    
    def random_create(self): # ランダムに作る
        itype = random.choice(["recovery"])
        return self.create(itype)