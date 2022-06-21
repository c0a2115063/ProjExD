from logging import root
import tkinter as tk
import tkinter.messagebox as tkm



def button_click(event):
    btn = event.widget
    txt = btn["text"]

    if txt == "=":
        eqn = entry.get()
        res = eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)

    else: 
        entry.insert(tk.END,txt)

if __name__ == "__main__":
    root  = tk.Tk()
    root.title("電卓")
    r = 1 #行番号   
    c = 0 #列番号

    entry = tk.Entry(root,justify="right",width=10, font=("Times New Roman",40))
    entry.grid(row=0,column=0,columnspan=3)

    for i,num in enumerate([9,8,7,6,5,4,3,2,1,0,"+","="]):
        button = tk.Button(root,
                           text=f"{num}", 
                           width=4, 
                           height=2, 
                           font=("Times New Roman", 30)
                           )
        button.bind("<1>",button_click)

        button.grid(row=r,column=c)
        c += 1
        if (i+1) % 3 == 0:
            r += 1
            c = 0
    
    root.mainloop()
