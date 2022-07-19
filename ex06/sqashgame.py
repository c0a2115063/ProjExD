import pygame as pg     #pygameモジュールを使用
import sys
import random

#グローバル変数
GameOver_falg = False
# //---------------Screenクラス -----------//
class Screen():     
    def __init__(self,title,size,backgroundimage):  #インスタンス変数
    #(ゲームタイトル,ゲーム画面,背景画像)
        pg.display.set_caption(title)
    #インスタンスメソッド
        self.surface = pg.display.set_mode(size)
        self.rect = self.surface.get_rect()
        self.background_surface = pg.image.load(backgroundimage)
        self.background_rect = self.background_surface.get_rect()

    def blit(self):
        self.surface.blit(self.background_surface,self.background_rect)

class Racket():
    def __init__(self,racket_image,expanding,racket_center): #インスタンス変数
    #(ラケットの色,ラケットのスピード,ラケットの中央座標)
    #インスタンスメソッド
        self.surface = pg.image.load(racket_image)
        self.surface = pg.transform.rotozoom(self.surface,0,expanding)
        self.rect = self.surface.get_rect()
        self.rect.center = racket_center

    def blit(self,screen:Screen):
        screen.surface.blit(self.surface,self.rect)

    def update(self,screen):
        key_states = pg.key.get_pressed() 
        if key_states[pg.K_LEFT]  ==  True:
            self.rect.centerx -= 1
        #左ボタンをクリックすると、X座標が-4される
        if key_states[pg.K_RIGHT] == True:
            self.rect.centerx += 1

        if check_bound(self.rect, screen.rect)!= (1, 1): # 領域外だったら
            if key_states[pg.K_LEFT]  == True: self.rect.centerx += 1
            if key_states[pg.K_RIGHT] == True: self.rect.centerx -= 1
        self.blit(screen)

class Ball():
    def __init__(self,ball_color,ball_r,ball_speed,screen):
        self.surface = pg.Surface((2*ball_r,2*ball_r))
        self.surface.set_colorkey((0,0,0))
        pg.draw.circle(self.surface,ball_color,(10,10),ball_r)
        self.rect = self.surface.get_rect()
        self.rect.centerx = 600 #random.randint(0,screen.background_rect.width)
        self.rect.centery = 300 #random.randint(0,screen.background_rect.height)
        self.vx ,self.vy = ball_speed
    
    def blit(self,screen):
        screen.surface.blit(self.surface,self.rect)
    
    def  update(self,screen):
        self.rect.move_ip(self.vx,self.vy)
        # 練習5
        self.surface.blit(self.surface, self.rect)
        # 練習7
        yoko, tate = check_bound(self.rect, screen.rect)
        self.vx *= yoko
        self.vy *= tate

        self.blit(screen)


# //-------------- main 関数 -----------------//
def main():
    screen = Screen("スカッシュゲーム",(1200,600),"fig/bg.png")
    racket = Racket("fig/missile.png", 2.0 ,((600,550)))
    ball = Ball((255,0,0), 10, (+1.0,+1.0),screen)

    while True:
        if GameOver_falg:  #ボールが最下点に達したら、GameOver_falgがTrueして、pygameが終了する
            return 
        else:    
            screen.blit()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return

            racket.blit(screen)
            racket.update(screen)

            
            ball.blit(screen)
            ball.update(screen)


            

            pg.display.update()



        

def check_bound(rect,screen_rect):
    global GameOver_falg

    yoko,tate = +1,+1
    if rect.left < screen_rect.left or screen_rect.right < rect.right:
        yoko = -1
    if rect.top < screen_rect.top:
        tate = -1

    if rect.bottom >  screen_rect.bottom:
        GameOver_falg = True

    return yoko,tate



if __name__ == "__main__":
    pg.init()

    main()
    pg.quit()
    sys.exit()
