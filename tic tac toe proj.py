from tkinter import *
from tkinter import messagebox
window=Tk()
window.title('Welcome')
window.geometry("400x400+100+100")
turn=1
def button1():
    global turn
    if btn1["text"]==" ":
        if turn==1:
           turn=2
           btn1["text"]="X"
        elif turn==2:
            turn=1
            btn1["text"]="O"
        check()
def button2():
    global turn
    if btn2["text"]==" ":
        if turn==1:
           turn=2
           btn2["text"]="X"
        elif turn==2:
            turn=1
            btn2["text"]="O"
        check()
def button3():
    global turn
    if btn3["text"]==" ":
        if turn==1:
           turn=2
           btn3["text"]="X"
        elif turn==2:
            turn=1
            btn3["text"]="O"
        check()
def button4():
    global turn
    if btn4["text"]==" ":
        if turn==1:
           turn=2
           btn4["text"]="X"
        elif turn==2:
            turn=1
            btn4["text"]="O"
        check()
def button5():
    global turn
    if btn5["text"]==" ":
        if turn==1:
           turn=2
           btn5["text"]="X"
        elif turn==2:
            turn=1
            btn5["text"]="O"
        check()
def button6():
    global turn
    if btn6["text"]==" ":
        if turn==1:
           turn=2
           btn6["text"]="X"
        elif turn==2:
            turn=1
            btn6["text"]="O"
        check()
def button7():
    global turn
    if btn7["text"]==" ":
        if turn==1:
           turn=2
           btn7["text"]="X"
        elif turn==2:
            turn=1
            btn7["text"]="O"
        check()
def button8():
    global turn
    if btn8["text"]==" ":
        if turn==1:
           turn=2
           btn8["text"]="X"
        elif turn==2:
            turn=1
            btn8["text"]="O"
        check()
def button9():
    global turn
    if btn9["text"]==" ":
        if turn==1:
           turn=2
           btn9["text"]="X"
        elif turn==2:
            turn=1
            btn9["text"]="O"
        check()

flag=1
def check():
    global flag
    b1=btn1["text"]
    b2=btn2["text"]
    b3=btn3["text"]
    b4=btn4["text"]
    b5=btn5["text"]
    b6=btn6["text"]
    b7=btn7["text"]
    b8=btn8["text"]
    b9=btn9["text"]
    flag=flag+1
    if b1==b2 and b1==b3 and b1=="X" or b1==b2 and b1==b3 and b1=="O":
        win(btn1["text"])
    if b4==b5 and b4==b6 and b4=="X" or b4==b5 and b4==b6 and b4=="O":
        win(btn4["text"])
    if b7==b8 and b7==b9 and b7=="X" or b7==b8 and b7==b9 and b7=="O":
        win(btn7["text"])
    if b1==b4 and b1==b7 and b1=="X" or b1==b4 and b1==b7 and b1=="O":
        win(btn1["text"])
    if b2==b5 and b2==b8 and b2=="X" or b2==b5 and b2==b8 and b2=="O":
        win(btn2["text"])
    if b3==b6 and b3==b9 and b3=="X" or b3==b6 and b3==b9 and b3=="O":
        win(btn3["text"])
    if b1==b5 and b1==b9 and b1=="X" or b1==b5 and b1==b9 and b1=="O":
        win(btn1["text"])
    if b3==b5 and b3==b7 and b3=="X" or b3==b5 and b3==b7 and b3=="O":
        win(btn3["text"])
    if flag==10:
        messagebox.showinfo("Tie","Match Tied! Try Again.")
        window.destroy()
def win(player):
    stringg="OVER! "+player+" WON THE GAME!"
    messagebox.showinfo("Congratulations",stringg)
    window.destroy()      
             
label1=Label(window,text='Tic-Tac-Toe Game',font=('Times New Roman','15'),fg='black')
label1.grid(row=0,column=0)
label2=Label(window,text='Player 1: X',font=('Times New Roman','10'),fg='black')
label2.grid(row=1,column=0)
label3=Label(window,text='Player 2: O',font=('Times New Roman','10'),fg='black')
label3.grid(row=2,column=0)
btn1=Button(text=" ",fg='white',bg='black',font=('Times New Roman','9'),height=5,width=5,command=button1)
btn1.grid(row=3,column=3)
btn2=Button(text=" ",fg='white',bg='black',font=('Times New Roman','9'),height=5,width=5,command=button2)
btn2.grid(row=3,column=4)
btn3=Button(text=" ",fg='white',bg='black',font=('Times New Roman','9'),height=5,width=5,command=button3)
btn3.grid(row=3,column=5)
btn4=Button(text=" ",fg='white',bg='black',font=('Times New Roman','9'),height=5,width=5,command=button4)
btn4.grid(row=4,column=3)             
btn5=Button(text=" ",fg='white',bg='black',font=('Times New Roman','9'),height=5,width=5,command=button5)
btn5.grid(row=4,column=4)             
btn6=Button(text=" ",fg='white',bg='black',font=('Times New Roman','9'),height=5,width=5,command=button6)
btn6.grid(row=4,column=5)
btn7=Button(text=" ",fg='white',bg='black',font=('Times New Roman','9'),height=5,width=5,command=button7)
btn7.grid(row=5,column=3)
btn8=Button(text=" ",fg='white',bg='black',font=('Times New Roman','9'),height=5,width=5,command=button8)
btn8.grid(row=5,column=4)             
btn9=Button(text=" ",fg='white',bg='black',font=('Times New Roman','9'),height=5,width=5,command=button9)
btn9.grid(row=5,column=5)             
