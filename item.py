import pygame as pg
import random, sound

'''
アイテムのスーパークラス
'''
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
    
    def playSound(self):
        pass
    
    '''
    更新処理
    '''
    def update(self):
        self._rect.x += self._vx
        self._rect.y += self._vy
        if self._rect.y > 650:
            self._is_existed = False
    
    '''
    描画処理
    '''
    def draw(self, screen):
        screen.blit(self._image, self._rect)

'''
ポーション（小回復アイテム）
回復量：50
落下速度：1-4
'''
class SmallRecoveryItem(Item):
    def __init__(self):
        super().__init__()
        self._image = pg.image.load("images/portion.png")
        self._hpRecovery = 50
    
    def playSound(self):
        sound.SoundManager.get_instance().plyarecoversmall()

'''
おにぎり（中回復アイテム）
回復量：100
落下速度：5-7
'''
class MediumRecoveryItem(Item):
    def __init__(self):
        super().__init__()
        self._image = pg.image.load("images/onigiri.png")
        self._hpRecovery = 100
        self._vy = random.uniform(5, 7)
    
    def playSound(self):
        sound.SoundManager.get_instance().plyarecovermedium()

'''
ドーナッツ（大回復アイテム）
回復量：150
落下速度：8-10
'''
class LargeRecoveryItem(Item):
    def __init__(self):
        super().__init__()
        self._image = pg.image.load("images/donuts.png")
        self._hpRecovery = 150
        self._vy = random.uniform(8, 10)

    def playSound(self):
        sound.SoundManager.get_instance().plyarecoverlarge()

'''
アイテムファクトリークラス
'''
class ItemFactory():
    def create(self, itype):
        if itype == "smallrecovery":
            return SmallRecoveryItem()
        if itype == "mediumrecovery":
            return MediumRecoveryItem()
        if itype == "largerecovery":
            return LargeRecoveryItem()
        return Item()
    
    '''
    ランダム生成
    '''
    def random_create(self):
        itype = random.choice(["smallrecovery", "mediumrecovery", "largerecovery"])
        return self.create(itype)