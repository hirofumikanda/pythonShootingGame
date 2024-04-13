import pygame as pg

'''
スタート画面
'''
class StartScene():
    def __init__(self, game):
        font = pg.font.Font(None, 50)
        self._game = game
        self._msg = font.render("Press SPACE to play.", True, pg.Color("WHITE"))
        self._gamestart = pg.image.load("images/gamestart.png")
    
    '''
    更新処理
    '''
    def update(self):
        key = pg.key.get_pressed()
        if key[pg.K_SPACE]:
            self._game.start()
    
    '''
    描画処理
    '''
    def draw(self, screen):
        screen.blit(self._msg, (120, 380))
        if self._game.is_started == False:
            screen.blit(self._gamestart, (50, 200))