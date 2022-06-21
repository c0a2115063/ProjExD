from logging import root
from this import s
import tkinter as tk
import tkinter.messagebox as tkm
import re                       #文字列の置換を行うために reメソッドをインポートした



def button_click(event):
    btn = event.widget
    txt = btn["text"]             

    if txt == "=":              # = が入力されたら計算が実行される          
        eqn = entry.get()
        if '×' in eqn:          #　×のボタンを入力すると
            reeqn = re.compile(r"×") # ×のマークから*の計算記号に変更
            eqn = reeqn.sub("*",eqn) #元の変数に代入

        if '÷' in eqn:          # ÷のボタンを入力すると
            reeqn = re.compile(r"÷") #÷のマークから/の計算記号に変更
            eqn = reeqn.sub("/",eqn) #元の変数に変更

        res = eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)

    else:                       # =以外の数字と+が入力されたら上のテキストに表示            
        entry.insert(tk.END,txt)

if __name__ == "__main__":
    root  = tk.Tk()
    root.title("カラフル電卓")
    r = 1 #行番号   
    c = 0 #列番号
    #入力したボタンの数字を画面に表示
    entry = tk.Entry(root,justify="right",width=10, font=("Times New Roman",40))
    entry.grid(row=0,column=0,columnspan=3)                                       #

    #ボタンの位置確認
    for i,num in enumerate([9,8,7,6,5,4,3,2,1,0,"+","-","×","÷","="]):#引き算と掛け算、割り算
        button = tk.Button(root,
                           text=f"{num}", 
                           width=3,      #幅を変更 
                           height=1,
                           bg= "blue",   #ボタンの背景色を青色に変更
                           fg = "green", #ボタンの文字の色を変更
                           font=("Times New Roman", 45)
                           )
        button.bind("<1>",button_click)

        button.grid(row=r,column=c)
        c += 1
        if (i+1) % 3 == 0:
            r += 1
            c = 0
    
    root.mainloop()
