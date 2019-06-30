from tkinter import *
import tkinter.messagebox
tk=Tk()
tk.title("Tic Tac Toe")
click=True

def checker(buttons):
    global click
    if buttons["text"]==" " and click==True:
        buttons["text"]="X"
        click=False
    elif buttons["text"]==" " and click==False:
          buttons["text"]="O"
          click=True

    elif (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X" or
         b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" or
         b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" or
         b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" or
         b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" or
         b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" or
         b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X" or
         b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X") :
          tkinter.messagebox.showinfo("Winner X","You won")


    elif (b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" or
         b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" or
         b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" or
         b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" or
         b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" or
         b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" or
         b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O" or
         b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O") :
          tkinter.messagebox.showinfo("Winner O", "You won")
    else:
        tkinter.messagebox.showinfo("Tie", "A Tie")



buttons=StringVar()
b1=Button(tk,text=" ",font=("TImes 26 bold"),height=4,width=8,command=lambda:checker(b1))
b1.grid(row=1,column=0,sticky=S+N+E+W)

b2=Button(tk,text=" ",font=("TImes 26 bold"),height=4,width=8,command=lambda:checker(b2))
b2.grid(row=1,column=1,sticky=S+N+E+W)

b3=Button(tk,text=" ",font=("TImes 26 bold"),height=4,width=8,command=lambda:checker(b3))
b3.grid(row=1,column=2,sticky=S+N+E+W)

b4=Button(tk,text=" ",font=("TImes 26 bold"),height=4,width=8,command=lambda:checker(b4))
b4.grid(row=2,column=0,sticky=S+N+E+W)

b5=Button(tk,text=" ",font=("TImes 26 bold"),height=4,width=8,command=lambda:checker(b5))
b5.grid(row=2,column=1,sticky=S+N+E+W)

b6=Button(tk,text=" ",font=("TImes 26 bold"),height=4,width=8,command=lambda:checker(b6))
b6.grid(row=2,column=2,sticky=S+N+E+W)

b7=Button(tk,text=" ",font=("TImes 26 bold"),height=4,width=8,command=lambda:checker(b7))
b7.grid(row=3,column=0,sticky=S+N+E+W)

b8=Button(tk,text=" ",font=("TImes 26 bold"),height=4,width=8,command=lambda:checker(b8))
b8.grid(row=3,column=1,sticky=S+N+E+W)

b9=Button(tk,text=" ",font=("TImes 26 bold"),height=4,width=8,command=lambda:checker(b9))
b9.grid(row=3,column=2,sticky=S+N+E+W)

tk.mainloop()