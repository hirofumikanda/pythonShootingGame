import pygame as pg

'''
結果表示
'''
class ResultScene():
    def __init__(self, game):
        font = pg.font.Font(None, 50)
        self._game = game
        self._msg = font.render("Press SPACE to end.", True, pg.Color("WHITE"))
        self._gameover = pg.image.load("images/gameover.png")
        self._gameclear = pg.image.load("images/gameclear.png")
        self._great = pg.image.load("images/great.png")
        self._pity = pg.image.load("images/pity.png")
    
    '''
    更新処理
    '''
    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_SPACE]:
            self._game.reset()
    
    '''
    描画処理
    '''
    def draw(self, screen):
        screen.blit(self._msg, (120, 100))
        if self._game.is_playing == False:
            # ゲームクリア時
            if self._game.is_cleared == True:
                screen.blit(self._gameclear, (50, 200))
                screen.blit(self._great, (237, 350))
            # ゲームオーバー時
            else:
                screen.blit(self._gameover, (50, 200))
                screen.blit(self._pity, (237, 350))