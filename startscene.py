import pygame as pg
import const

'''
スタート画面
'''
class StartScene():
    def __init__(self, game):
        font = pg.font.Font(None, 30)
        self._game = game
        self._msg = font.render("Press E(Easy) or N(Normal) or H(Hard) to play.", True, pg.Color("WHITE"))
        self._gamestart = pg.image.load("images/gamestart.png")
    
    '''
    更新処理
    '''
    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_e]:
            self._game.start(const.Constants().get_instance().EASY)
        if key[pg.K_n]:
            self._game.start(const.Constants().get_instance().NORMAL)
        if key[pg.K_h]:
            self._game.start(const.Constants().get_instance().HARD)
    
    '''
    描画処理
    '''
    def draw(self, screen):
        screen.blit(self._msg, (70, 380))
        if self._game.is_started == False:
            screen.blit(self._gamestart, (50, 200))