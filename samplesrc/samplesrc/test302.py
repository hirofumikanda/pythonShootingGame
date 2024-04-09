# 1.準備
import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((600, 650))
pg.display.set_caption("MYGAME")
player = pg.image.load("images/kaeru1.png")
myrect = pg.Rect(250, 550, 50, 50)
# 2.メインループ
while True:
    # 3.画面の初期化
    screen.fill(pg.Color("NAVY"))
    # 4.入力チェックや判断処理
    # 5.描画処理
    screen.blit(player, myrect)
    # 6.画面の表示
    pg.display.update()
    # 7.閉じるボタンチェック
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()