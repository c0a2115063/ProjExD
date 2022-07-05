from random import randint
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

#練習3
    koukaton_sfc = pg.image.load("fig/6.png")   #surface
    koukaton_sfc = pg.transform.rotozoom(koukaton_sfc, 0, 2.0) #surface
    koukaton_rect = koukaton_sfc.get_rect()     #rect
    koukaton_rect.center = 900, 400

#練習５：爆弾
    bomb_sfc = pg.Surface((20,20))  #surface

    bomb_sfc.set_colorkey((0, 0 ,0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)

    bomb_rect = bomb_sfc.get_rect()     #rect
    bomb_rect.centerx = randint(0, screen_rect.width)
    bomb_rect.centery = randint(0, screen_rect.height)

    #練習6
    vx,vy = +1 , +1

    while True:
        screen_sfc.blit(bg_img,bg_rect)
        
        #練習２
        for event in pg.event.get():    #イベントを繰り返して処理
            if event.type == pg.QUIT:   #ウインドウのXボタンがクリックされたら
                return

        #練習4
        key_states = pg.key.get_pressed()

        if key_states[pg.K_UP] == True:#y座標を-1
            koukaton_rect.centery -= 1
        
        if key_states[pg.K_DOWN] == True:#y座標を+1
            koukaton_rect.centery += 1
        
        if key_states[pg.K_LEFT] == True:#x座標を-1
            koukaton_rect.centerx -= 1 
        
        if key_states[pg.K_RIGHT] == True:#x座標を+1
            koukaton_rect.centerx += 1
        
        #練習7
        if check_bound(koukaton_rect,screen_rect) != (1,1):
            if key_states[pg.K_UP] == True:#y座標を-1
                koukaton_rect.centery += 1
        
            if key_states[pg.K_DOWN] == True:#y座標を+1
                koukaton_rect.centery -= 1
            
            if key_states[pg.K_LEFT] == True:#x座標を-1
                koukaton_rect.centerx += 1 
            
            if key_states[pg.K_RIGHT] == True:#x座標を+1
                koukaton_rect.centerx -= 1

        screen_sfc.blit(koukaton_sfc,koukaton_rect)
        
        #練習６
        bomb_rect.move_ip(vx,vy)
        
        #練習5
        screen_sfc.blit(bomb_sfc,bomb_rect)

        #練習7
        yoko, tate = check_bound(bomb_rect,screen_rect)

        vx *= yoko

        vy *= tate       

        #練習8
        if koukaton_rect.colliderect(bomb_rect):
            return
        if bomb_rect.colliderect(koukaton_rect):
            return

        pg.display.update()
        clock.tick(1000)
#練習７  
def check_bound(rect,scr_rect):     #rect: こうかとんと爆弾のRect   scr_rect:スクリーンのRect
    yoko,tate = +1,+1
    if rect.left < scr_rect.left or scr_rect.right < rect.right :
        yoko = -1
    if rect.top < scr_rect.top or scr_rect.bottom < rect.bottom :
        tate = -1
    return yoko,tate




if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()