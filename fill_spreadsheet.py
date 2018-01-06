import gspread
import random
import sys
import time
import array
from oauth2client.service_account import ServiceAccountCredentials

#test statements
'''
print(chr(0))
print(chr(65))
print(ord(chr(65)))
'''
w = (sys.argv)
name = (w[1])
wksn = (w[2])
ed = ('Insert your email here')

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

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
#(temp) sheet = client.open("Survey_Project_Responses").sheet1
''' temporary opening: '''
#sh = gc.open(name_old)

''' stuff: '''

#This is to create a spreadsheet if it cannot be opened
try:
	gc.open(name)
except gspread.exceptions.SpreadsheetNotFound:

	sh = gc.create(name)
	sh.share(ed, perm_type='user', role='writer')

gc.open(name)
#for worksheet creation
sh = gc.open(name)

#For the parsing of the row
sh2 = gc.open(name).sheet1

#This is to create a worksheet if a worksheet cannot be opened
try:
	sh.worksheet(wksn)

except gspread.exceptions.WorksheetNotFound:
	worksheet = sh.add_worksheet(title=str(wksn), rows="100", cols="26")

sh.worksheet(wksn)

''' end of stuff '''

wks = sh.worksheet(wksn)
wks2 = client.open(name).sheet1

n2 = 1

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

'''
EXAMPLE:
worksheet.update_cell(1, 2, 'Bingo!')

''' 

#print (wks.cell(1, 1).value)

while ((wks.row_values(d)[0]) != ''):
	d += 1

for i in range((len(w)-3)):
	if (n != (len(w))):
		con = w[n]
	else:
		con = ('error')		
	wks.update_cell((d), (n-2), con)
	if (n != (len(w))):
		n += 1


#(temp)print (d)
#(temp)print (n)
#(temp)print (con)
