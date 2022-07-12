from turtle import update
import pygame as pg
import sys
import random

class Screen():
    def __init__(self,title,width,bg_image):
        
        # 練習1：スクリーンと背景画像
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(width) # Surface
        self.rct = self.sfc.get_rect()            # Rect
        self.bgi_sfc = pg.image.load(bg_image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()              # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

class Bird():
    def __init__(self,image:str,expanding,bird_center):
        # 練習2：こうかとん
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, expanding)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = bird_center

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]    == True:
            self.rct.centery -= 5
        if key_states[pg.K_DOWN]  == True:
            self.rct.centery += 5
        if key_states[pg.K_LEFT]  == True:
            self.rct.centerx -= 5
        if key_states[pg.K_RIGHT] == True: 
            self.rct.centerx += 5

        # 練習7
        if check_bound(self.rct, scr.rct)!= (1, 1): # 領域外だったら
            if key_states[pg.K_UP]    == True: self.rct.centery += 5
            if key_states[pg.K_DOWN]  == True: self.rct.centery -= 5
            if key_states[pg.K_LEFT]  == True: self.rct.centerx += 5
            if key_states[pg.K_RIGHT] == True: self.rct.centerx -= 5
        self.blit(scr)

class Bomb():
    def __init__(self,color,r,speed,scr:Screen):
        # 練習5：爆弾
        self.sfc = pg.Surface((2*r, 2*r)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (10, 10), r)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.bgi_rct.width)
        self.rct.centery = random.randint(0, scr.bgi_rct.height)
        self.vx, self.vy = speed      # 練習6

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr:Screen):
        self.rct .move_ip(self.vx,self.vy)
        # 練習5
        self.sfc.blit(self.sfc, self.rct)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate

        self.blit(scr)

class Bomb2():
    def __init__(self,color,r,speed,scr:Screen):
        # 練習5：爆弾
        self.sfc = pg.Surface((2*r, 2*r)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (10, 10), r)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.bgi_rct.width)
        self.rct.centery = random.randint(0, scr.bgi_rct.height)
        self.vx, self.vy = speed      # 練習6

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr:Screen):
        self.rct .move_ip(self.vx,self.vy)
        # 練習5
        self.sfc.blit(self.sfc, self.rct)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate

        self.blit(scr)


class Missile():
    def __init__(self,image, kkt):
        self.sfc = pg.image.load(image)
        ### 画像サイズ変更
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 2.0)

        ### ミサイルオブジェクト生成
        self.rct = self.sfc.get_rect()

        ### ミサイル初期位置
        self.rct.centerx = kkt.rct.centerx
        self.rct.centery = kkt.rct.centery
    
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

    ############################
    ### ミサイル移動
    ############################
    def update(self, surface):
        ### ミサイル速度
        #key_states = pg.key.get_pressed()
        self.rct.centerx -= 5
        self.blit(surface)

def main():
    clock = pg.time.Clock()
    #練習1
    scr = Screen("逃げろ！こうかとん",(1600,900),"fig/pg_bg.jpg")

    kkt = Bird("fig/6.png",2.0,((900,400)))
    kkt.update(scr)

    bkd = Bomb((255,0,0), 10, (+5,+5),scr)
    bkd2 = Bomb2((0,255,0), 20, (+5,+5),scr)

    missile = None 

    while True:
        scr.blit()

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_states = pg.key.get_pressed()
        if key_states[pg.K_SPACE] == True:
            missile = Missile("fig/missile.png",kkt)

        if missile:
            missile.update(scr)
            

        kkt.update(scr)
        kkt.blit(scr)

        bkd.update(scr)
        bkd.blit(scr)

        bkd2.update(scr)
        bkd2.blit(scr)


        

        # 練習8
        if kkt.rct.colliderect(bkd.rct) :
            return
        
        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()