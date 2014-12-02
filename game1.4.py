from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')

finish = drawpad.create_rectangle(0, 0, 75, 50, fill="green")

e1 = drawpad.create_rectangle(0,540,425,570, fill="white", outline="white")
e2 = drawpad.create_rectangle(700,500,800,600, fill="white", outline="white")
e3 = drawpad.create_rectangle(700,0,800,560, fill="white", outline="white")
e4 = drawpad.create_rectangle(300,150,450,300, fill="white", outline="white")
e5 = drawpad.create_rectangle(250,0,550,50, fill="white", outline="white")
e6 = drawpad.create_rectangle(110,190,160,470, fill="white", outline="white")
e7 = drawpad.create_rectangle(500,430,550,495, fill="white", outline="white")
e8 = drawpad.create_rectangle(230,180,290,240, fill="white", outline="white")
hint1 = drawpad.create_rectangle(300,580,310,600, fill="white", outline="white")
player = drawpad.create_oval(390,580,410,600, fill="blue")
#collisionDetect == false

enemyList =[e1, e2, e3, e4, e5, e6, e7, e8]

    


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
        if self.collisionDetect2() == True:
            sx1,sy1,sx2,sy2 = 390,580,410,600
            print "u tuk a rong turn m8" 
            drawpad.move(player,sx1 - x1, sy1 - y1)
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

    def collisionDetect2(self): 
        global player   
        rx1,ry1,rx2,ry2 = drawpad.coords(player)
        for x in enemyList:
            ex1,ey1,ex2,ey2 = drawpad.coords(x)
            if (rx1 >= ex1 and rx2 <= ex2) and (ry1 >= ey1 and ry2 <= ey2):
                print "found enemy"
                return True

    def collisionDetect(self):
        global player
        global finish
        rx1,ry1,rx2,ry2 = drawpad.coords(player)
        x1, y1, x2, y2 = drawpad.coords(finish)
        if (rx1 >= x1 and rx2 <= x2) and (ry1 >= y1 and ry2 <= y2):
            return True
        
            
        

app = myApp(root)
root.mainloop()