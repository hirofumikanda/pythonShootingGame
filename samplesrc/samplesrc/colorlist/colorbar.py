import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))
colors = []
for c in pg.color.THECOLORS:
    colors.append(c)
font = pg.font.Font(None, 22)
startID = 0

while True:
    screen.fill(pg.Color("WHITE"))
    textimg = font.render("Up/Down keys to move.", True, pg.Color("BLACK"))
    screen.blit(textimg, (300, 560))
    n = startID
    for i in range(11):
        for j in range(5):
            if (n < len(colors)):
                c = pg.Color(colors[n])
                x = j * 150 + 30
                y = i * 50
                pg.draw.rect(screen, c, (x, y, 140, 40))
                textimg = font.render(colors[n], True, pg.Color("BLACK"))
                screen.blit(textimg, (x + 5, y + 4))
                textimg = font.render(colors[n], True, pg.Color("WHITE"))
                screen.blit(textimg, (x + 5, y + 20))
                n += 1
    key = pg.key.get_pressed()
    if key[pg.K_DOWN]:
        startID = startID + 5
        if startID > len(colors):
            startID = len(colors) - 2
    if key[pg.K_UP]:
        startID = startID - 5
        if startID < 0:
            startID = 0
    pg.display.update()
    pg.time.Clock().tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()