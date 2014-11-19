from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')

finish = drawpad.create_rectangle(0, 0, 75, 50, fill="green")
player = drawpad.create_oval(390,580,410,600, fill="blue")
enemny1 = drawpad.create_rectangle(390,550,410,570, fill="white", outline="white")
#collisionDetect == false
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
        rx1,ry1,rx2,ry2 = drawpad.coords(finish)
        x1,y1,x2,y2 = drawpad.coords(player)
        if self.collisionDetect() == True:
            print "good job youve made it"  
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
    def collisionDetect(self):
        global player
        global finish
        rx1,ry1,rx2,ry2 = drawpad.coords(player)
        x1, y1, x2, y2 = drawpad.coords(finish)
        
        if (rx1 >= x1 and rx2 <= x2) and (ry1 >= y1 and ry2 <= y2):
            return True
            
            
        

app = myApp(root)
root.mainloop()