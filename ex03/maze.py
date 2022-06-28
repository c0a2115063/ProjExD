import tkinter as tk



if __name__ == "__main__":
    key = ""
    root = tk.Tk()
    root.title("迷えるこうかとん")

    Canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    Canvas.pack()

    bird = tk.PhotoImage(file="fig/6.png")
    cx,cy = 300,400
    Canvas.create_image(cx,cy,image=bird,tag="bird")
    
    root.mainloop()