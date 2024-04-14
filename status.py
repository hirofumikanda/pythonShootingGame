import pygame as pg
import const

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
    
    @property
    def distance(self):
        return self._distance

    '''
    初期化処理
    '''
    def reset(self):
        self._font = pg.font.Font(None, 32)
        self._distance = 0
        self._score = 0
        self._level = const.Constants.get_instance().EASY
    
    '''
    更新処理
    '''
    def update(self, ntype):
        if ntype == "distance":
            self._distance += 2
        if ntype == "score":
            self._score += 1
        if ntype == "level":
            self._level += 1
    
    '''
    描画処理
    '''
    def draw(self, screen):
        pg.draw.rect(self._board, (0, 0, 0, 128), pg.Rect(0, 0, 800, 36))
        screen.blit(self._board, (0, 0))

        info1 = self._font.render(f"DISTANCE : {self._distance}", True, pg.Color("WHITE"))
        screen.blit(info1, (20, 10))
        
        levelDisp = self.getLevelDescription()
        info2 = self._font.render(f"LEVEL : {levelDisp}", True, pg.Color("WHITE"))
        screen.blit(info2, (230, 10))

        info3 = self._font.render(f"SCORE : {self._score}", True, pg.Color("WHITE"))
        screen.blit(info3, (450, 10))
    
    def getLevelDescription(self):
        if self._level == const.Constants.get_instance().EASY:
            return "EASY"
        if self._level == const.Constants.get_instance().NORMAL:
            return "NORMAL"
        if self._level == const.Constants.get_instance().HARD:
            return "HARD"