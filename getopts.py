import os
import sys
import argparse

# getopts is an adapter for fill_spreadsheets.py that conditions each double quoted argument in a form
# that Python appears to like. IOW, this program handles some (but not all) of the cross language runtime
# environment nonsense (on Windows - it might be more straightforward on MacOS or linux).
parser = argparse.ArgumentParser(
                description='Text file conversion.'
                )


comma_delimited_args = ""

if len(sys.argv) < 6:
    print("getopts - not enough arguments - exiting")
    sys.exit(1)

def print_it():
    os.system("../fill_spreadsheet.py " + sys.argv[2] + " " + sys.argv[3] + " "  + comma_delimited_args)
    
argc = 4
for arg in sys.argv[argc:]:
    # print (x)
    comma_delimited_args += '"' + arg + '"'
    if ( argc < len(sys.argv)-1):
        comma_delimited_args += " "
    argc=argc+1

print("comma_delimited_args[" + str(argc) + "]=[" + comma_delimited_args + "]")

cmd = "python ./fill_spreadsheet.py "  + sys.argv[1] + " "  + sys.argv[2] + " " + sys.argv[3] + " " + comma_delimited_args

print ("cmd=" + cmd)
os.system(cmd)


# args = parser.parse_args()    # This is messed up and doesn't work very well- see https://docs.python.org/3/library/argparse.html
# print("args='" + str(type(args)) )    # NOPE