import pygame as pg
import sys

def main():

    clock = pg.time.Clock() #時間計測用のオブジェクト

    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900))  #surface 1600,900の背景
    screen_rect = screen_sfc.get_rect()          #rect
    bg_img = pg.image.load("fig/pg_bg.jpg")   #surface
    bg_rect = bg_img.get_rect()
    screen_sfc.blit(bg_img,bg_rect)

#課題3
    koukaton_sfc = pg.image.load("fig/6.png")   #surface
    koukaton_sfc = pg.transform.rotozoom(koukaton_sfc, 0, 2.0) #surface
    koukaton_rect = koukaton_sfc.get_rect()     #rect
    koukaton_rect.center = 900, 400

    while True:
        screen_sfc.blit(bg_img,bg_rect)
        screen_sfc.blit(koukaton_sfc,koukaton_rect)
        #練習２
        for event in pg.event.get():    #イベントを繰り返して処理
            if event.type == pg.QUIT:   #ウインドウのXボタンがクリックされたら
                return

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()