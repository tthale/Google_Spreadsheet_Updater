# Very basic (non-OptionMenu with callbacks) menu UI 
from Tkinter import *
# Say hi to jproperties, which helps this program create .properties files!
from jproperties import Properties

choices = { 'Math','Science','Religion','English','Arts'}   # Dictionary with options
vertical_placement = 45             # first row starting position
vertical_placement_increment = 20   # Increment for next row
first_column_postion = 65
second_column_postion = 140
third_column_position = 200
vert_dimen = 200
fin_button_vert_pos = 135
selections = [] # FInal selection list of classes
selection_codes = []
double_matrix_selections = [[]] # TODO - TOm - decide to use over selections & selection_codes
uname = ""
pwd = ""


def closeWin():
    global uname
    global pwd
    
    uname = e.get()
    pwd = d.get()
    
    z.close()
    exam.destroy()

def grab_and_assign (event):
    global vertical_placement
    global vert_dimen
    global exam
    global be
    global fin_button_vert_pos
    class_code = class_entry.get()
    fin_button_vert_pos += vertical_placement_increment
    vert_dimen += vertical_placement_increment
    exam.geometry("360x" + str(vert_dimen) + "+400+300") #adjusts window height
    be.place(x = 130, y = fin_button_vert_pos)
    
    '''
    print str(event)
    print(class_code)
    '''
    
    selections.append(str(event))
    selection_codes.append(str(class_code))
    # TDOO - exam.geometry("360x200+400+300")    <- need to adjust geometry every iteration
    #be.place(x = 130, y = 135 + vertical_placement_increment) --> This was bad
    vertical_placement += vertical_placement_increment
    p = Label(exam, text = "Class:  ")
    p.place(x = first_column_postion, y = vertical_placement)
    tkvar = StringVar(exam) # Create a Tkinter variable
    drop_menu = OptionMenu(exam, tkvar,  *choices, command=grab_and_assign)
    # drop_menu.grid(row=3, column=2)    <= NOPE, stuck @ 0,0
    drop_menu.place(x = second_column_postion, y = vertical_placement)
    # TODO2: Add a new input field on the next class row

# Start execution here
z = open("exam.txt", "w")

exam = Tk()
exam.title("Please Input your Information")
exam.geometry("360x200+400+300")
string_var = StringVar()

u = Label(exam, text="User Name:  ")
u.place(x = first_column_postion, y = vertical_placement)
e = Entry(exam, textvariable = string_var, bd = 3)
e.place(x= second_column_postion, y = vertical_placement)

vertical_placement += vertical_placement_increment
p = Label(exam, text = "Password:  ")
p.place(x = first_column_postion, y = vertical_placement)
d = Entry(exam, bd = 3, show="*")
d.place(x= second_column_postion, y = vertical_placement)

vertical_placement += vertical_placement_increment
p = Label(exam, text = "Class:  ")
p.place(x = first_column_postion, y = vertical_placement)
tkvar = StringVar(exam) # Create a Tkinter variable
drop_menu = OptionMenu(exam, tkvar,  *choices, command=grab_and_assign)
# drop_menu.grid(row=3, column=2)    <= NOPE, stuck @ 0,0
drop_menu.place(x = second_column_postion, y = vertical_placement)
class_var = StringVar()
class_entry = Entry(exam, textvariable = class_var, bd = 3)
class_entry.place(x= third_column_position, y = vertical_placement)

be = Button(exam, text="Finish", width = 14, height = 2, fg="black", command=closeWin)
be.place(x = 130, y = 135)

exam.mainloop()
# ^^^ closes the tkinter setup

classes = ""
classids = ""

prop = Properties()

for i in selections:
    classes = classes + i + " "
    
for i in selection_codes:
    classids = classids + i + " "
#classes from classlist are added into one string, so that it can work with jproperties. 

#p["foobar"] = "A very important message from our sponsors: Python is great!"
prop["classnames"] = classes[0:(len(classes)-1)] #inputs all the class names, w/o the space at the end
prop["classids"] = classids[0:(len(classids)-1)]   #inputs all the class_ids, w/o the space at the end
prop["Username"] = uname
prop["Password"] = pwd

#for the .properties file, spaces are put in to demarcate where each class name/ class id starts and stops

with open ("classes.properties", "wb") as f: # opens the .properties file as a write-to file and then puts classes & classids in
    #another thing, wb means write, while rb means read. Not sure what the "b" is supposed to be
    #p.load(f, "utf-8")
    prop.store(f, encoding="utf-8")
    #This ends the program, by setting in stone the writes this program makes
