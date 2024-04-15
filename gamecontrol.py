import pygame as pg
import player, enemy, bullet, status, sound, item, const, logging, resultstore

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
        # ロギング設定
        logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s", filename="play.log")
        
        self._player = player.Player()
        self._enemies = []
        self._items = []
        self._effects = []
        self._bullets = []
        self._enemyfactory = enemy.EnemyFactory()
        self._itemfactory = item.ItemFactory()
        self._bulletfactory = bullet.BulletFactory()
        self._status = status.Status.get_instance()
        self.attach(self._status)
        self.reset()
    
    @property
    def is_playing(self):
        return self._is_playing
    @property
    def is_cleared(self):
        return self._is_cleared
    @property
    def is_started(self):
        return self._is_started
    
    '''
    初期表示又はゲーム終了からスタート画面に戻るときの初期化処理
    '''
    def reset(self):
        self._is_playing = False
        self._is_cleared = False
        self._is_started = False
        self._level = const.Constants.get_instance().EASY
        self._player.reset()
        self._enemies.clear()
        self._items.clear()
        self._spawn_count = 0
        self._spawn_count_items = 0
        self._bullets.clear()
        self._bullet_count = 0
        self._bullet_level = 0
        self._status.reset()
        for i in range(2):
            self._enemies.append(enemy.Enemy())
        for i in range(1):
            self._enemies.append(enemy.FlameEnemy())
        for i in range(1):
            self._enemies.append(enemy.IceEnemy())
        # 案内音声再生
        sound.SoundManager.get_instance().playstartannounce()

    '''
    更新処理
    '''
    def update(self):
        # 距離表示更新
        self.notify("distance")

        # aキーが押されていた場合は一定間隔で弾丸追加
        self._bullet_count += 1
        if self._bullet_count > 10:
            key = pg.key.get_pressed()
            if key[pg.K_a]:
                self._bullets.append(self._bulletfactory.create(self._player.rect, self._bullet_level))
                self._bullet_count = 0
        
        # エフェクト処理更新（敵と弾丸衝突時の爆発エフェクト）
        for e in self._effects:
            e.update()
        
        # 弾丸移動
        for b in self._bullets:
            b.update()

        # プレイヤー移動
        self._player.update()

        # 一定間隔で敵キャラを増やす
        self._spawn_count += 1
        if self._spawn_count > const.Constants.get_instance().ENEMYINTERVAl(self._level):
            self._spawn_count = 0
            self._enemies.append(self._enemyfactory.random_create(self._level))
        
        # 一定間隔でアイテムを増やす
        self._spawn_count_items += 1
        if self._spawn_count_items > const.Constants.get_instance().ITEMINTERVAL(self._level):
            self._spawn_count_items = 0
            self._items.append(self._itemfactory.random_create(self._level))

        for e in self._enemies:
            for b in self._bullets:

                # 敵と弾丸が衝突したときの敵のダメージ処理
                if e.rect.colliderect(b.rect):
                    sound.SoundManager.get_instance().playattack()
                    self._bullets.remove(b)
                    e.hp -= b.attack
                    if e.hp <= 0:
                        for i in range(e.score):
                            self.notify("score")
                            if self._status.score % 10 == 0 and self._status.score != const.Constants.get_instance().CLEARNUMBER(self._level):
                                sound.SoundManager.get_instance().playencourage()
                            if self._status.score == const.Constants.get_instance().CLEARNUMBER(self._level) - 5:
                                sound.SoundManager.get_instance().playencourage_last()
                        b = enemy.BombEffect(e.rect, self._effects)
                        sound.SoundManager.get_instance().playblast()
                        self._effects.append(b)
                        self._enemies.remove(e)
                        
                        # ゲームクリア処理
                        if self._status.score >= const.Constants.get_instance().CLEARNUMBER(self._level): # クリア条件
                            self._is_playing = False
                            self._is_cleared = True
                            logging.info(f"{self._status.getLevelDescription()}:{self._status.distance}")
                            sound.SoundManager.get_instance().bgmstop()
                            sound.SoundManager.get_instance().playclear()
                            resultstore.ResultStore.get_instance().appendToResultFile(self._level, self._status.distance)

            # 敵が下に落ちていたら削除
            if e.is_alive == False:
                self._enemies.remove(e)
                break

            e.update()

            # 敵が下に落ちたら削除
            if e.rect.y >= 650:
                self._enemies.remove(e)

            # 敵と主人公が衝突した時の主人公のダメージ処理
            if e in self._enemies:
                if e.rect.colliderect(self._player.rect):
                    sound.SoundManager.get_instance().playbomb()
                    self._enemies.remove(e)
                    self._player.damage()
                    self._player.hp -= e.attack

                    # ゲームオーバー処理
                    if self._player.hp <= 0:
                        self._is_playing = False
                        logging.info(f"Level:{self._status.getLevelDescription()} - Distance:{self._status.distance} - Score:{self._status.score}")
                        sound.SoundManager.get_instance().bgmstop()
                        sound.SoundManager.get_instance().playover()
        
        for i in self._items:
            
            i.update()

            # アイテムが下に落ちたら削除
            if i.rect.y >= 650:
                self._items.remove(i)
            
            # アイテムと主人公が衝突した時のアイテム効果処理
            if i in self._items:
                if i.rect.colliderect(self._player.rect):
                    i.playSound()
                    self._items.remove(i)
                    self._player.hp += i.hpRecovery
                    if self._player.hp >= self._player.maxhp:
                        self._player.hp = self._player.maxhp
                    if i.improveWeapon == True:
                        if self._bullet_level < const.Constants.get_instance().MAX_BULLET_LEVEL:
                            self._bullet_level += 1
                    if i.magicApply == True: # 敵を全滅させる
                        sound.SoundManager.get_instance().plyaMagic()
                        for e in self._enemies:
                            for i in range(e.score):
                                self.notify("score")
                                if self._status.score % 10 == 0 and self._status.score != const.Constants.get_instance().CLEARNUMBER(self._level):
                                    sound.SoundManager.get_instance().playencourage()
                                if self._status.score == const.Constants.get_instance().CLEARNUMBER(self._level) - 5:
                                    sound.SoundManager.get_instance().playencourage_last()
                            b = enemy.BombEffect(e.rect, self._effects)
                            sound.SoundManager.get_instance().playblast()
                            self._effects.append(b)
                            self._enemies.remove(e)

    '''
    描画処理
    '''
    def draw(self, screen):
        for b in self._bullets:
            b.draw(screen)
        for e in self._effects:
            e.draw(screen)
        self._player.draw(screen)
        for e in self._enemies:
            e.draw(screen)
        for i in self._items:
            i.draw(screen)
        self._status.draw(screen)
    
    '''
    ゲームスタート時の処理
    '''
    def start(self, level):
        self._is_playing = True
        self._is_started = True
        self._level = level
        if self._level == const.Constants.get_instance().NORMAL:
            self.notify("level")
        if self._level == const.Constants.get_instance().HARD:
            self.notify("level")
            self.notify("level")
        sound.SoundManager.get_instance().bgmstart()