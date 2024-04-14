import pygame as pg
import random, sound, const

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
        self._improveWeapon = False

    @property
    def rect(self):
        return self._rect
    
    @property
    def hpRecovery(self):
        return self._hpRecovery
    
    @property
    def improveWeapon(self):
        return self._improveWeapon
    
    '''
    SE再生
    '''
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
        sound.SoundManager.get_instance().playrecoversmall()

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
        sound.SoundManager.get_instance().playrecovermedium()

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
        sound.SoundManager.get_instance().playrecoverlarge()

'''
武器（武器強化アイテム）
回復量：0
武器強化フラグ：True
落下速度：8-10
'''
class StrongWeaponItem(Item):
    def __init__(self):
        super().__init__()
        self._image = pg.image.load("images/weapon.png")
        self._improveWeapon = True
        self._vy = random.uniform(8, 10)
    
    def playSound(self):
        sound.SoundManager.get_instance().playimprove()
        
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
        if itype == "strongweapon":
            return StrongWeaponItem()
        return Item()
    
    '''
    ランダム生成
    '''
    def random_create(self, level):
        itypeArray = []
        itypeDict = const.Constants.get_instance().ITEMTYPE(level)
        for key, value in itypeDict.items():
            for i in range(value):
                itypeArray.append(key)
        itype = random.choice(itypeArray)
        return self.create(itype)