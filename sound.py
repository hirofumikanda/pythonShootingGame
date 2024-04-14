import pygame as pg
import random, time

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
        self._welcome = pg.mixer.Sound("sounds/welcome.mp3")
        self._choose = pg.mixer.Sound("sounds/choose.mp3")
        self._over = pg.mixer.Sound("sounds/over.wav")
        self._over1 = pg.mixer.Sound("sounds/over1.mp3")
        self._over2 = pg.mixer.Sound("sounds/over2.mp3")
        self._clear = pg.mixer.Sound("sounds/clear.wav")
        self._clear1 = pg.mixer.Sound("sounds/clear1.mp3")
        self._clear2 = pg.mixer.Sound("sounds/clear2.mp3")
        self._clear3 = pg.mixer.Sound("sounds/clear3.mp3")
        self._clap1 = pg.mixer.Sound("sounds/clap1.wav")
        self._clap2 = pg.mixer.Sound("sounds/clap2.wav")
        self._clap3 = pg.mixer.Sound("sounds/clap3.wav")
        self._blast = pg.mixer.Sound("sounds/blast.wav")
        self._bomb = pg.mixer.Sound("sounds/bomb.wav")
        self._recover1 = pg.mixer.Sound("sounds/recover1.mp3")
        self._recover2 = pg.mixer.Sound("sounds/recover2.mp3")
        self._recover3 = pg.mixer.Sound("sounds/recover3.mp3")
        self._encourage1 = pg.mixer.Sound("sounds/encourage1.mp3")
        self._encourage2 = pg.mixer.Sound("sounds/encourage2.mp3")
        self._encourage3 = pg.mixer.Sound("sounds/encourage3.mp3")
    
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
        overSound = random.choice([self._over1, self._over2])
        overSound.play()
    
    '''
    ゲームクリア音
    '''
    def playclear(self):
        clearSound = random.choice([self._clear1, self._clear2, self._clear3])
        clearSound.play()
    
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
    
    '''
    ようこそ
    '''
    def playstartannounce(self):
        self._welcome.play()
        time.sleep(2)
        self._choose.play()
    
    '''
    応援
    '''
    def playencourage(self):
        encourageSound = random.choice([self._encourage1, self._encourage2, self._encourage3])
        encourageSound.play()