import pygame as pg

'''
弾丸クラス
'''
class Bullet():
    def __init__(self, rect):
        x = rect.x + 17
        y = rect.y - 10
        self._image = pg.image.load("images/bullet.png")
        self._rect = self._image.get_rect()
        self._rect.topleft = (x, y)
        self._vy = -8
        self._is_alive = True
    
    @property
    def rect(self):
        return self._rect
    @rect.setter
    def rect(self, value):
        self._rect = value
    
    '''
    更新処理
    '''
    def update(self):
        self._rect.y += self._vy
        if self._rect.y < -100:
            self._is_alive = False
    
    '''
    描画処理
    '''
    def draw(self, screen):
        screen.blit(self._image, self._rect)

'''
強化弾丸クラス
'''
class StrongBullet(Bullet):
    def __init__(self, rect):
        super().__init__(rect)
        x = rect.x
        y = rect.y - 30
        self._image = pg.image.load("images/bullet_strong.png")
        self._rect = self._image.get_rect()
        self._rect.topleft = (x, y)