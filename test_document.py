from Tkinter import *

def closeWin():
    print (w)
    print (r)
    z.close()
    exam.destroy()

z = open("exam.txt", "w")

exam = Tk()
exam.title("Please Input your Information")
exam.geometry("360x200+400+300")
string_var = StringVar()

u = Label(exam, text="User Name:  ")
u.place(x = 65, y = 45)
e = Entry(exam, textvariable = string_var, bd = 3)
e.place(x= 140, y = 45)

p = Label(exam, text = "Password:  ")
p.place(x = 65, y = 85)
d = Entry(exam, bd = 3, show="*")
d.place(x = 140, y = 85)

w = e.get()
r = d.get()

be = Button(exam, text="Finish", width = 14, height = 2, fg="black", command=closeWin)
be.place(x = 130, y = 135)

exam.mainloop()
