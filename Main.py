import Lib as a
from tkinter import *

def buttonencode():
    print(t1.get("1.0","end"))
    t2.delete('1.0',"end")
    t2.insert("1.0",a.encoding(t1.get("1.0","end")[:-1]))
    

def buttondecode():
    t2.delete('1.0',"end")
    try:
        t2.insert("1.0",a.decoding(t1.get("1.0","end")))
    except:
        t2.insert("1.0","错误!")


window = Tk()
window.title("反李乐谦编码")
window.resizable(False,False)
window.geometry('500x300')

l1= Label(window,text="输入")
l1.place(x=110,y=10)

l2= Label(window,text="结果")
l2.place(x=360,y=10)

t1=Text(window,width=32, height=17)
t1.place(x=10,y=30)

t2=Text(window,width=32, height=17)
t2.place(x=260,y=30)

b1=Button(window,text="编码",command=buttonencode)
b1.place(x=200,y=265)

b2=Button(window,text="解码",command=buttondecode)
b2.place(x=260,y=265)

window.mainloop()

    
