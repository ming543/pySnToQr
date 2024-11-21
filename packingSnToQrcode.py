import os
import tkinter
import time
import keyboard
#import pyWinFunc
#import pyautogui

snQty = 00

window = tkinter.Tk()
window.title("包裝序號轉QRCODE")
window.minsize(width=1280, height=500)
window.resizable(width=False, height=False)

snCountLabel = tkinter.Label(text="包裝序號輸入量 %2d" %snQty, font=("Arial", 14, "bold"), padx=5, pady=5, bg="blue", fg="yellow")
snCountLabel.place(x=10,y=100)

snInputLabel = tkinter.Label(text="輸入包裝序號", font=("Arial", 14, "bold"), padx=5, pady=5, bg="blue", fg="yellow")
snInputLabel.place(x=10,y=10)

#snShow = tkinter.StringVar()
#snShowLabel = tkinter.Label(window, textvariable=snShow)
snShowLabel = tkinter.Label(window)
snShowLabel.place(x=10,y=150)


snInput = tkinter.Entry(window)
snInput.place(x=180,y=20)

#txt = tkinter.Text(window, relief="ridge", bd=8, fg="Black", font=("Arial", 14, "bold"))
#txt.place(x=400, y=10, relwidth=0.55, relheight=0.95)
snList = []


def snInputGet(e):
    global snQty 
    global snCountLabel
    global snShowLabel
    global snList
    snQty += 1
    #text.delete(0, END)
    value = snInput.get()
    snList.append(value)
    print(snList)
    #txt.insert('1.0', value)
    #snShow.set(value)
    snShowLabel.destroy() 
    snShowLabel = tkinter.Label(window, text = snList)
    snShowLabel.place(x=10,y=150)
    #snShowLabel.pack()
    #label= tkinter.Label(window, text= value)
    #label.pack()
    snInput.delete(0, tkinter.END)
    #snCountLabel.destroy()
    snCountLabel = tkinter.Label(text="包裝序號輸入量 %2d" %snQty, font=("Arial", 14, "bold"), padx=5, pady=5, bg="blue", fg="yellow")
    snCountLabel.place(x=10,y=100)

     

def handler(e):
    #text.delete(0, END)
    value = snInput.get()
    #txt.insert('1.0', value)
    label= tkinter.Label(window, text= value)
    label.pack()
    snInput.delete(0, tkinter.END)


def buttonQr():
    global snQty 
    global snCountLabel
    global snShowLabel
    global snList
    
    #snCountLabel.config(text="Hello World!")
    #txt.insert('1.0', "Hello World!\n\n")
    #txt.insert('2.0', "*" * 42)
    #time.sleep(0.2)
    #txt.delete('1.0', tkinter.END)   
    
    #清除包裝總數量
    snQty = 0
    snCountLabel.destroy()
    snCountLabel = tkinter.Label(text="包裝序號輸入量 %2d" %snQty, font=("Arial", 14, "bold"), padx=5, pady=5, bg="blue", fg="yellow")
    snCountLabel.place(x=10,y=100)
    
    #清除LABEL內容
    snShowLabel.destroy()
    #snShowLabel.config(text = '')    
    #snShowLabel = tkinter.Label.after(1000, label.destroy)
    #snShowLabel.pack()
    #label.pack()
    snList = []


        

button = tkinter.Button(text="產生QRCODE", font=("Arial", 14, "bold"), padx=5, pady=5, bg="blue", fg="light green", command=buttonQr)
button.place(x=10,y=300)

menu = tkinter.Menu()
window.config(menu=menu)

menuSystem = tkinter.Menu(activebackground="green", activeborderwidth=10, borderwidth=20)
menu.add_cascade(label="menuSystem", menu=menuSystem) # add menu
#menuSystem.add_command(label="mouseLocGet", command=mouseLocGet_clicked)


#menuSystem.add_separator() # 新增分隔符
#menuSystem.add_command(label="label2") # add label2


#Bind the Enter Key to Call an event
window.bind('<Return>',snInputGet)
#window.bind('<Return>',handler)


window.mainloop()