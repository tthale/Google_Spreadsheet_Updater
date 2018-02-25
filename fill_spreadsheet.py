import gspread
import pygsheets
import random
import sys
import time
import array
import googleapiclient
from oauth2client.service_account import ServiceAccountCredentials
import os
#test statements
'''
print(chr(0))
print(chr(65))
print(ord(chr(65)))
'''
w = (sys.argv)
name = (w[1])
wksn = (w[2])
ed = os.environ['google_spreadsheet_sharing']
sec = os.environ['secrets']

value = w
for v in range(3):
	value.pop(0)
	
#Old version using gspread
'''
#wksn = ((time.strftime("%m/%d/%Y")))
name_old = str(2872116359)

#+', '+(time.strftime("%H:%M:%S")))

#(str(random.getrandbits(32)))

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

	sh = gc.create(name, parent_id = None)
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
l = ['cell1','cell2','cell3','cell4','cell5','cell6','cell7','cell8','cell9','cell10']
'''
Temporary Commenting Out
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

#This is the new way the program determines which row to input on:
try:

	while ((wks.get_value((d,1))) != ''):
		d += 1

except pygsheets.exceptions.CellNotFound:
	d += 1

#This inserts new rows in, and also could be repeated multiple times because it increases the boundaries of the worksheet itself:
wks.insert_rows((d-1), number = 1, values=value, inherit = False)

#This gives a bold format to the first row of the worksheet, it can be disabled without any complications arising:
try:
	if (wks.get_value('Z1') == ''):
		wks.update_cell('Z1', 'Bolded')
		for i in range(1,10):
			wks.cell((1,i)).set_text_format('bold', True)

except googleapiclient.errors.HttpError:
	hi = 'Hi Mom!'


#This is the end, however some more edits may occur in the future.