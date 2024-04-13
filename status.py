import pygame as pg

'''
オブザーバースーパークラス
'''
class Observer:
    def update(self, ntype):
        pass

'''
ゲームステータスクラス
'''
class Status(Observer):
    def __init__(self):
        self.reset()
        self._board = pg.Surface((800, 36), pg.SRCALPHA)
    
    @property
    def score(self):
        return self._score

    '''
    初期化処理
    '''
    def reset(self):
        self._font = pg.font.Font(None, 32)
        self._distance = 0
        self._score = 0
    
    '''
    更新処理
    '''
    def update(self, ntype):
        if ntype == "distance":
            self._distance += 2
        if ntype == "score":
            self._score += 1
    
    '''
    描画処理
    '''
    def draw(self, screen):
        pg.draw.rect(self._board, (0, 0, 0, 128), pg.Rect(0, 0, 800, 36))
        screen.blit(self._board, (0, 0))
        info1 = self._font.render(f"DISTANCE : {self._distance}", True, pg.Color("WHITE"))
        info2 = self._font.render(f"SCORE : {self._score}", True, pg.Color("WHITE"))
        screen.blit(info1, (20, 10))
        screen.blit(info2, (450, 10))