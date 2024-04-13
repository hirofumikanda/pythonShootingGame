import pygame as pg
import random

'''
サウンドマネージャークラス
'''
class SoundManager():
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def __init__(self):
        pg.mixer.music.load("sounds/bgm.wav")
        self._over = pg.mixer.Sound("sounds/over.wav")
        self._clear = pg.mixer.Sound("sounds/clear.wav")
        self._clap1 = pg.mixer.Sound("sounds/clap1.wav")
        self._clap2 = pg.mixer.Sound("sounds/clap2.wav")
        self._clap3 = pg.mixer.Sound("sounds/clap3.wav")
        self._blast = pg.mixer.Sound("sounds/blast.wav")
        self._bomb = pg.mixer.Sound("sounds/bomb.wav")
        self._recover1 = pg.mixer.Sound("sounds/recover1.mp3")
        self._recover2 = pg.mixer.Sound("sounds/recover2.mp3")
        self._recover3 = pg.mixer.Sound("sounds/recover3.mp3")
    
    '''
    BGM再生
    '''
    def bgmstart(self):
        pg.mixer.music.play(-1)
    
    '''
    BGM停止
    '''
    def bgmstop(self):
        pg.mixer.music.stop()

    '''
    ゲームオーバー音
    '''    
    def playover(self):
        self._over.play()
    
    '''
    ゲームクリア音
    '''
    def playclear(self):
        self._clear.play()
    
    '''
    主人公攻撃音
    '''
    def playattack(self):
        r = random.randint(0, 3)
        if r == 0:
            self._clap1.play()
        elif r == 1:
            self._clap2.play()
        else:
            self._clap3.play()
    
    '''
    敵破壊音
    '''
    def playblast(self):
        self._blast.play()
    
    '''
    主人公爆発音
    '''
    def playbomb(self):
        self._bomb.play()
    
    '''
    小回復音
    '''
    def plyarecoversmall(self):
        self._recover1.play()
    
    '''
    中回復音
    '''
    def plyarecovermedium(self):
        self._recover2.play()
    
    '''
    大回復音
    '''
    def plyarecoverlarge(self):
        self._recover3.play()