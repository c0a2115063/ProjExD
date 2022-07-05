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
    koukaton_sfc = pg.image.load("fig/3.png")   #surface               
    koukaton_sfc2 = pg.image.load("fig/11.png") #surface
    
    koukaton_sfc = pg.transform.rotozoom(koukaton_sfc, 0, 2.0) #surface
    koukaton_sfc2 = pg.transform.rotozoom(koukaton_sfc2,0,2.0) #surface 
    ###こうかとんが右に移動するときに画像左右反転する
   

    
    koukaton_rect = koukaton_sfc.get_rect()     #rect
    koukaton_rect.center = 900, 400

#練習５：爆弾
    bomb_sfc = pg.Surface((80,80))  #surface

    bomb_sfc.set_colorkey((0, 0 ,0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (40, 40), 40)     #爆弾の大きさを変更

    bomb_rect = bomb_sfc.get_rect()     #rect
    bomb_rect.centerx = randint(0, screen_rect.width)
    bomb_rect.centery = randint(0, screen_rect.height)

    ###緑色の爆弾追加
    bomb_sfc2 = pg.Surface((80,80))  #surface
    bomb_sfc2.set_colorkey((0, 0 ,0))
    pg.draw.circle(bomb_sfc2, (0, 0, 255), (40, 40), 40)     #爆弾の大きさを変更

    bomb_rect2 = bomb_sfc2.get_rect()     #rect
    bomb_rect2.centerx = randint(0, screen_rect.width)
    bomb_rect2.centery = randint(0, screen_rect.height)

    ###青色の爆弾追加
    bomb_sfc3 = pg.Surface((80,80))  #surface
    bomb_sfc3.set_colorkey((0, 0 ,0))
    pg.draw.circle(bomb_sfc3, (0, 255, 0), (40, 40), 40)     #爆弾の大きさを変更

    bomb_rect3 = bomb_sfc3.get_rect()     #rect
    bomb_rect3.centerx = randint(0, screen_rect.width)
    bomb_rect3.centery = randint(0, screen_rect.height)

    #練習6
    vx,vy =   +3, +3             #爆弾の加速度を3に変更
    ###緑色の爆弾の加速度を追加
    vx2,vy2 = +4, +4
    ###青色の爆弾の加速度を追加
    vx3,vy3 = +5, +5

    while True:
        screen_sfc.blit(bg_img,bg_rect)
        
        #練習２
        for event in pg.event.get():    #イベントを繰り返して処理
            if event.type == pg.QUIT:   #ウインドウのXボタンがクリックされたら
                return

        #練習4
        key_states = pg.key.get_pressed()

        if key_states[pg.K_UP] == True:#y座標を-1
            koukaton_rect.centery -= 5              ###こうかとんの加速度を５に変更
        
        if key_states[pg.K_DOWN] == True:#y座標を+1
            koukaton_rect.centery += 5
        
        if key_states[pg.K_LEFT] == True:#x座標を-1
            koukaton_rect.centerx -= 5 

        if key_states[pg.K_RIGHT] == True:#x座標を+1
            koukaton_rect.centerx += 5
            ###こうかとんの画像を変更
            screen_sfc.blit(koukaton_sfc2,koukaton_rect)

        else:
            screen_sfc.blit(koukaton_sfc,koukaton_rect)

        #練習7
        if check_bound(koukaton_rect,screen_rect) != (1,1):
            if key_states[pg.K_UP] == True:#y座標を+1
                koukaton_rect.centery += 5
        
            if key_states[pg.K_DOWN] == True:#y座標を-1
                koukaton_rect.centery -= 5
            
            if key_states[pg.K_LEFT] == True:#x座標を+1
                koukaton_rect.centerx += 5 

            if key_states[pg.K_RIGHT] == True:#x座標を-1
                koukaton_rect.centerx -= 5
                
        
        #練習６
        ###爆弾の動きを2つ追加
        bomb_rect.move_ip(vx,vy)
        bomb_rect2.move_ip(vx2,vy2)
        bomb_rect3.move_ip(vx3,vy3)
        #練習5
        ###爆弾を画面にblitを2つ追加
        screen_sfc.blit(bomb_sfc,bomb_rect)
        screen_sfc.blit(bomb_sfc2,bomb_rect2)
        screen_sfc.blit(bomb_sfc3,bomb_rect3)

        #練習7
        yoko1, tate1 = check_bound(bomb_rect,screen_rect)
        vx *= yoko1
        vy *= tate1

        ###緑色の爆弾のチェックバウンド
        yoko2, tate2 = check_bound(bomb_rect2,screen_rect)
        vx2 *= yoko2
        vy2 *= tate2
        ###青色の爆弾のチェックバウンド
        yoko3, tate3 = check_bound(bomb_rect3,screen_rect)
        vx3 *= yoko3
        vy3 *= tate3      

        #練習8
        if koukaton_rect.colliderect(bomb_rect):
            return
        if koukaton_rect.colliderect(bomb_rect2):
            return
        if koukaton_rect.colliderect(bomb_rect3):
            return
        if bomb_rect.colliderect(koukaton_rect):
            return
        if bomb_rect2.colliderect(koukaton_rect):
            return
        if bomb_rect3.colliderect(koukaton_rect):
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