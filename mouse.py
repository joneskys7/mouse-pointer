import Tkinter as tk
root = tk.Tk()

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
    print "x=",x
    print "y=",y
    
    if x>y:
       print "A is greater"
    if x<y:
       print "B is greater"
    if x==y:
        print"Both are equal"
root.bind('<Motion>', motion)
root.mainloop()
