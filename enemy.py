import pygame as pg
import random, const

'''
ノーマルモンスター（他のモンスターのスーパークラス）
最大HP：100
攻撃：50
落下速度：1-4
撃墜スコア：1
'''
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
        self._attack = 50
        self._score = 1

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
    @property
    def attack(self):
        return self._attack
    @property
    def score(self):
        return self._score

    '''
    更新処理
    '''
    def update(self):
        if self._rect.x < 0 or self._rect.x > 550:
            self._vx = -self._vx
        self._rect.x += self._vx
        self._rect.y += self._vy
        if self._rect.y > 650:
            self._is_alive = False
    
    '''
    描画処理
    '''
    def draw(self, screen):
        screen.blit(self._image, self._rect)
        # hpbar
        rect1 = pg.Rect(self._rect.x, self._rect.y - 20, 4, 20)
        h = (self._hp / self._maxhp) * 20
        rect2 = pg.Rect(self._rect.x, self._rect.y - h, 4, h)
        pg.draw.rect(screen, pg.Color("RED"), rect1)
        pg.draw.rect(screen, pg.Color("GREEN"), rect2)

'''
炎のモンスター
最大HP：100
攻撃：50
落下速度：5-7
撃墜スコア：1
'''
class FlameEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self._image = pg.image.load("images/enemy2.png")
        self._vx = random.uniform(-2, 2)
        self._vy = random.uniform(5, 7)

'''
氷のモンスター
最大HP：150
攻撃：50
落下速度：1-4
撃墜スコア：1
'''
class IceEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self._image = pg.image.load("images/enemy3.png")
        self._maxhp = 150
        self._hp = 150

'''
炎のモンスター２
最大HP：100
攻撃：100
落下速度：5-7
撃墜スコア：1
'''
class StrongFlameEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self._image = pg.image.load("images/enemy4.png")
        self._vx = random.uniform(-2, 2)
        self._vy = random.uniform(5, 7)
        self._attack = 100

'''
ドラゴン
最大HP：150
攻撃：150
落下速度：5-7
撃墜スコア：2
'''
class DragonEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self._image = pg.image.load("images/enemy5.png")
        self._vx = random.uniform(-2, 2)
        self._vy = random.uniform(5, 7)
        self._attack = 150
        self._maxhp = 150
        self._hp = 150
        self._score = 2

'''
弾丸との衝突時の爆発エフェクト
'''
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
    
    '''
    更新処理
    '''
    def update(self):
        self._cnt += 1
        idx = self._cnt
        if idx <= 5:
            self._image = self._images[idx]
        else:
            self._effects.remove(self)
    
    '''
    描画処理
    '''
    def draw(self, screen):
        screen.blit(self._image, self._rect)

'''
敵キャラファクトリークラス
'''
class EnemyFactory():
    def create(self, etype):
        if etype == "flame":
            return FlameEnemy()
        if etype == "ice":
            return IceEnemy()
        if etype == "strongflame":
            return StrongFlameEnemy()
        if etype == "dragon":
            return DragonEnemy()
        return Enemy()
    
    '''
    ランダム生成
    '''
    def random_create(self, level):
        etypeArray = []
        etypeDict = const.Constants().get_instance().ENEMYTYPE(level)
        for key, value in etypeDict.items():
            for i in range(value):
                etypeArray.append(key)
        etype = random.choice(etypeArray)
        return self.create(etype)