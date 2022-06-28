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
    if key == "Down" and maze_bg[my+1][mx] == 0:
        my += 1
    if key == "Left" and maze_bg[my][mx-1] == 0:
        mx -= 1
    if key == "Right" and maze_bg[my][mx+1] == 0:
        mx += 1
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

    bird = tk.PhotoImage(file="fig/6.png")
    mx ,my = 1,1
    cx,cy = 100+50,100+50
    Canvas.create_image(cx,cy,image=bird,tag="bird")
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()