import pygame as pg
import const, logging
from pygame.locals import *

'''
スタート画面
'''
class StartScene():
    def __init__(self, game):
        # ロギング設定
        logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
        font = pg.font.Font(None, 50)
        self._game = game
        self._msg = font.render("Choose Level to PLAY", True, pg.Color("WHITE"))
        self._gamestart = pg.image.load("images/gamestart.png")
        self._easyButton = pg.image.load("images/EasyButton.png")
        self._normalButton = pg.image.load("images/NormalButton.png")
        self._hardButton = pg.image.load("images/HardButton.png")
    
    '''
    更新処理
    '''
    def update(self):
        mouseX, mouseY = pg.mouse.get_pos()
        mBtnL, mBtnC, mBtnR = pg.mouse.get_pressed()
        if mBtnL == 1:
            # Easyボタン
            if 125 <= mouseX and mouseX <= 475 and 130 <= mouseY and mouseY <= 230:
                self._game.start(const.Constants.get_instance().EASY)
                return
            # Normalボタン
            if 125 <= mouseX and mouseX <= 475 and 270 <= mouseY and mouseY <= 370:
                self._game.start(const.Constants.get_instance().NORMAL)
                return
            # Hardボタン
            if 125 <= mouseX and mouseX <= 475 and 410 <= mouseY and mouseY <= 510:
                self._game.start(const.Constants.get_instance().HARD)
                return
    
    '''
    描画処理
    '''
    def draw(self, screen):
        screen.blit(self._msg, (120, 60))
        if self._game.is_started == False:
            # screen.blit(self._gamestart, (50, 200))
            screen.blit(self._easyButton, (125,130))
            screen.blit(self._normalButton, (125, 270))
            screen.blit(self._hardButton, (125, 410))