from jproperties import Properties

curclass = "AP Calc BC"
curclassid = "8008135"
classlist = ["AP_Calc_BC", "AP_Physics_1", "AP_Statistics"]
classidlist = [ "8008135", "123456", "07082002"]

classes = ""
classids = ""

prop = Properties()

for i in classlist:
    classes = classes + i + " "
    
for i in classidlist:
    classids = classids + i + " "
#classes from classlist are added into one string, so that it can work with jproperties. 

#p["foobar"] = "A very important message from our sponsors: Python is great!"

prop["classnames"] = classes[0:(len(classes)-1)] #inputs all the class names, w/o the space at the end
prop["classids"] = classids[0:(len(classids)-1)]   #inputs all the class_ids, w/o the space at the end

#for the .properties file, spaces are put in to demarcate where each class name/ class id starts and stops

with open ("classes.properties", "wb") as f: # opens the .properties file as a write-to file and then puts classes & classids in
    #another thing, wb means write, while rb means read. Not sure what the "b" is supposed to be
    #p.load(f, "utf-8")
    prop.store(f, encoding="utf-8")
    #This ends the program, by setting in stone the writes this program makes