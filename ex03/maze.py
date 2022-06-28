import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx,cy,mx,my
    if key == "Up" and maze_bg[my-1][mx] == 0:
        my -= 1
        Canvas.delete("bird")                               #画像更新で処理が遅くなってしまうため、前の画像を削除する
        Canvas.create_image(cx,cy,image=bird_up,tag="bird") #上に移動する画像を出力

    if key == "Down" and maze_bg[my+1][mx] == 0:
        my += 1
        Canvas.delete("bird")                               #画像更新で処理が遅くなってしまうため、前の画像を削除する
        Canvas.create_image(cx,cy,image=bird_down,tag="bird")#下に移動する画像を出力

    if key == "Left" and maze_bg[my][mx-1] == 0:
        mx -= 1
        Canvas.delete("bird")                               #画像更新で処理が遅くなってしまうため、前の画像を削除する
        Canvas.create_image(cx,cy,image=bird_left,tag="bird")#左に移動する画像を出力

    if key == "Right" and maze_bg[my][mx+1] == 0:
        mx += 1
        Canvas.delete("bird")                               #画像更新で処理が遅くなってしまうため、前の画像を削除する
        Canvas.create_image(cx,cy,image=bird_right,tag="bird")#右に移動する画像を出力

    else:
        pass
    cx,cy = mx*100+50 , my*100+50
    Canvas.coords("bird",cx,cy)
    root.after(100,main_proc)

if __name__ == "__main__":
    key = ""
    root = tk.Tk()
    root.title("迷えるこうかとん")

    Canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    Canvas.pack()
    maze_bg = mm.make_maze(15,9)#壁：1 / 床：2を表す二次元リスト
    mm.show_maze(Canvas,maze_bg)#canvasにmaze_bgを描く
    bird = tk.PhotoImage(file="fig/0.png")
    bird_up = tk.PhotoImage(file="fig/3.png")  #上に移動するときのこうかとんの画像
    bird_down = tk.PhotoImage(file="fig/4.png")#下に移動するときのこうかとんの画像
    bird_left = tk.PhotoImage(file="fig/5.png")#左に移動するときのこうかとんの画像
    bird_right = tk.PhotoImage(file="fig/2.png")#右に移動するときのこうかとんの画像

    Canvas.create_rectangle(100,100,200,200,fill='red')
    Canvas.create_rectangle(1300,700,1400,800,fill='blue')

    mx ,my = 1,1
    cx,cy = 100+50,100+50
    Canvas.create_image(cx,cy,image=bird,tag="bird")
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()