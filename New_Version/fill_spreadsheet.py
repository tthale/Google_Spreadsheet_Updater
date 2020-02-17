# import gspread
import pygsheets
import random
import sys
import time
import array
import googleapiclient
from oauth2client.service_account import ServiceAccountCredentials
import os
from Tkinter import *
#test statements
'''
Fill a spreadsheet's (new or existing) worksheet with a single row's worth of cells. These are provided
as command line argumemnts separated by a space (if a cell is multi-word, then enclose each cell argument in double quotes)
Example:
"Spreadsheet name" "Worksheet Name" "first column info" "2nd col" "Look over 3rd col info" "4th col" " " "6th col" ...
'''
w = (sys.argv)
name = (w[1])
wksn = (w[2])
ed = os.environ['google_spreadsheet_sharing']
sec = os.environ['secrets']

# Strip off the first few args and keep just the cell data for the row to be added 
value = w
for v in range(3):
	value.pop(0)
	
#Old version using gspread
'''
+

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

client = gspread.authorize(creds)
gc = gspread.authorize(creds)
'''
#These are used to authorize any functions accessing google spreadsheets
#gc = pygsheets.authorize(something, no_cache = True)
gc = pygsheets.authorize(sec, no_cache=True)

''' temporary opening: '''
#sh = gc.open(name_old)

''' stuff: '''

#This is to create a spreadsheet if it cannot be opened
try:
	gc.open(name)
except pygsheets.SpreadsheetNotFound:

	gc.create(name, parent_id = None)
	sh = gc.open(name)
	sh.share(ed, role='writer')

#for worksheet editing
sh = gc.open(name)

#This is to create a worksheet if a worksheet cannot be opened
try:
	sh.worksheet_by_title(wksn)

except pygsheets.WorksheetNotFound:
	worksheet = sh.add_worksheet(title=str(wksn), rows="100", cols="26", src_tuple=None, src_worksheet=None)

wks = sh.worksheet_by_title(wksn)
''' end of stuff '''

#Old Example Array
'''
w = ['Mary', 'had', 'a', 'little', 'lamb', 'its', 'fleece', 'was', 'white', 'as', 'snow', 'and', 'everywhere', 'that', 'Mary', 'went', 'The', 'lamb', 'was', 'sure', 'to', 'go']
'''

d = 1
c = 0
c2 = 0
line = 1
n = 0

row_header = ['Course_Name','Course_Date','Homework_Item','HW_Due_Date','Status','Submission','Comments','Misc','cell9','cell10']


'''
Temporary Commenting Out
# branch 'master' of https://github.com/tthale/Google_Spreadsheet_Updater.git
if ((wks.row_values(d)[0]) == ''):
	for i in range(len(l)):
		if (n != (len(l))):
			con = l[n]
		else:
			con = ('error')
		wks.update_cell((d), (n+1), con)
		if (n != (len(l))):
			n += 1

n = 3


(Old) EXAMPLE:
worksheet.update_cell(1, 2, 'Bingo!')

#This is a function telling the value of cell A1:
print (wks.cell(1, 1).value)

#This is the old system to tell which row to insert on:
while ((wks.row_values(d)[0]) != ''):
	d += 1

#This used to input values per cell in the row:
for i in range((len(w)-3)):
	if (n != (len(w))):
		con = w[n]
	else:
		con = ('error')		
	wks.update_cell((d), (n-2), con)
	if (n != (len(w))):
		n += 1

'''

# Skip to the last row of the worksheet:
try:

	while ((wks.get_value((d,1))) != ''):
		d += 1

except pygsheets.exceptions.CellNotFound:
	d += 1
except IndexError:	# Indicative of this being a new worksheet; starts at d == 1
	if d == 1:
		wks.insert_rows(0, number = 1, values=row_header, inherit = False)
		d += 1

#This inserts new rows in, and also could be repeated multiple times because it increases the boundaries of the worksheet itself:
wks.insert_rows((d-1), number = 1, values=value, inherit = False)

#This gives a bold format to the first row of the worksheet, it can be disabled without any complications arising:
'''
try:
	if (wks.get_value('Z1') == ''):
		wks.update_cell('Z1', 'Bolded')
		for i in range(1,10):
			wks.cell((1,i)).set_text_format('bold', True)

except googleapiclient.errors.HttpError:
	hi = 'Hi Mom!'
'''

#This is the end, however some more edits may occur in the future.
