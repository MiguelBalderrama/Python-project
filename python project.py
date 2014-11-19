from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="blue")
class myApp(object):
    def __init__(self, parent):
        global rockets
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()
        drawpad.pack()
        root.bind_all('<Key>', self.key)
    
    def key(self,event):
        global player
        x1,x2,y1,y2 = drawpad.coords(player)
        if event.char == "w":
            if y1 > 0:
                drawpad.move(player,0,-4)
            else:
                return
        if event.char == "s":
            if y2 < 600:
                drawpad.move(player,0,4)
            else:
                return
        if event.char == "a":
            if x1 > 0:
                drawpad.move(player,-4,0)
            else:
                return
        if event.char == "d":
            if x2 < 800:
                drawpad.move(player,4,0)
            else:
                return

app = myApp(root)
root.mainloop()