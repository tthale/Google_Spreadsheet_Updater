from Tkinter import *

def doSomething():
    print("Hoi there!")

exam = Tk()

'''
menu = Menu(exam)
exam.config(menu=menu)
subMenu = Menu(menu) 
subMenu=Menu(menu,tearoff=0)
menu.add_cascade(label="file", menu=subMenu)
subMenu.add_command(label="New Project...", command=doSomething())
subMenu.add_command(label="New...", command=doSomething())
subMenu.add_separator()
subMenu.add_command(label="Exit",command=doSomething())
'''

exam.mainloop()