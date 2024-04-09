import pygame as pg
import random, player, enemy, bullet, status, sound

class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, ntype):
        for observer in self._observers:
            observer.update(ntype)

class GameManager(Subject):
    def __init__(self):
        super().__init__()
        self._player = player.Player()
        self._enemies = []
        self._effects = []
        self._bullets = []
        self._factory = enemy.EnemyFactory()
        self._status = status.Status()
        self.attach(self._status)
        self.reset()
    
    @property
    def is_playing(self):
        return self._is_playing
    @property
    def is_cleared(self):
        return self._is_cleared
    
    def reset(self): # ゲームのリセット
        self._is_playing = True
        self._is_cleared = False
        self._player.reset()
        self._enemies.clear()
        self._spawn_count = 0
        self._bullets.clear()
        self._bullet_count = 0
        self._status.reset()
        sound.SoundManager.get_instance().bgmstart()
        for i in range(2):
            self._enemies.append(enemy.Enemy())
        for i in range(1):
            self._enemies.append(enemy.FlameEnemy())
        for i in range(1):
            self._enemies.append(enemy.IceEnemy())

    def update(self): # 更新処理
        self.notify("distance")
        self._bullet_count += 1
        if self._bullet_count > 10:
            key = pg.key.get_pressed()
            if key[pg.K_a]:
                self._bullets.append(bullet.Bullet(self._player.rect))
                self._bullet_count = 0
        for e in self._effects:
            e.update()
        for b in self._bullets:
            b.update()
        self._player.update()
        self._spawn_count += 1
        if self._spawn_count > 15: # 敵発生量
            self._spawn_count = 0
            self._enemies.append(self._factory.random_create())
        for e in self._enemies:
            for b in self._bullets:
                if e.rect.colliderect(b.rect):
                    sound.SoundManager.get_instance().playattack()
                    self._bullets.remove(b)
                    e.hp -= 50
                    if e.hp <= 0:
                        self.notify("score")
                        b = enemy.BombEffect(e.rect, self._effects)
                        sound.SoundManager.get_instance().playblast()
                        self._effects.append(b)
                        self._enemies.remove(e)
                        if self._status.score == 30: # クリア条件
                            self._is_playing = False
                            self._is_cleared = True
                            sound.SoundManager.get_instance().bgmstop()
                            sound.SoundManager.get_instance().playclear()
            if e.is_alive == False:
                self._enemies.remove(e)
                break
            e.update()
            # 敵が下に落ちたら停止
            if e.rect.y >= 650:
                self._enemies.remove(e)

            # 敵と主人公が衝突したら、敵を上に移動
            if e in self._enemies:
                if e.rect.colliderect(self._player.rect):
                    sound.SoundManager.get_instance().playbomb()
                    self._enemies.remove(e)
                    self._player.damage()
                    self._player.hp -= 50
                    if self._player.hp <= 0:
                        self._is_playing = False
                        sound.SoundManager.get_instance().bgmstop()
                        sound.SoundManager.get_instance().playover()
        
    def draw(self, screen): # 描画処理
        for b in self._bullets:
            b.draw(screen)
        for e in self._effects:
            e.draw(screen)
        self._player.draw(screen)
        for e in self._enemies:
            e.draw(screen)
        self._status.draw(screen)