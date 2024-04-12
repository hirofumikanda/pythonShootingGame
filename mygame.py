# 準備
import pygame as pg, sys
import gamecontrol, resultscene, startscene
pg.init()
screen = pg.display.set_mode((600, 650))
pg.display.set_caption("Shooting Game")
game = gamecontrol.GameManager()
result = resultscene.ResultScene(game)
start = startscene.StartScene(game)

# メインループ
while True:
    # 画面初期化
    screen.fill(pg.Color("NAVY"))

    # 入力チェックや判断処理
    if game.is_playing == True:
        game.update()
    else:
        if game.is_started == True:
            result.update()
        else:
            start.update()

    # 描画処理
    game.draw(screen)
    if game.is_playing == False: # プレイ中ではない
        if game.is_started == False: # まだゲームスタートしていない
            start.draw(screen)
        else:
            result.draw(screen)

    # 画面の表示
    pg.display.update()
    pg.time.Clock().tick(60)

    # 閉じるボタンチェック
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()