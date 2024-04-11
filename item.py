import pygame as pg
import random

# アイテムスーパークラス
class Item():
    def __init__(self):
        x = random.randint(100, 500)
        y = -100
        self._image = pg.image.load("images/portion.png")
        self._rect = pg.Rect(x, y, 50, 50)
        self._vx = 0
        self._vy = random.uniform(1, 4)
        self._hpRecovery = 0

    @property
    def rect(self):
        return self._rect
    
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

# 小回復アイテム
class SmallRecoveryItem(Item):
    def __init__(self):
        super().__init__()
        self._image = pg.image.load("images/portion.png")
        self._hpRecovery = 50

# 中回復アイテム
class MediumRecoveryItem(Item):
    def __init__(self):
        super().__init__()
        self._image = pg.image.load("images/onigiri.png")
        self._hpRecovery = 100
        self._vy = random.uniform(5, 7)

# 大回復アイテム
class LargeRecoveryItem(Item):
    def __init__(self):
        super().__init__()
        self._image = pg.image.load("images/donuts.png")
        self._hpRecovery = 150
        self._vy = random.uniform(8, 10)

class ItemFactory():
    def create(self, itype): # タイプ指定で作る
        if itype == "smallrecovery":
            return SmallRecoveryItem()
        if itype == "mediumrecovery":
            return MediumRecoveryItem()
        if itype == "largerecovery":
            return LargeRecoveryItem()
        return Item()
    
    def random_create(self): # ランダムに作る
        itype = random.choice(["smallrecovery", "mediumrecovery", "largerecovery"])
        return self.create(itype)