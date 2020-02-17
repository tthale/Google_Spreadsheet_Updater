import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Open a worksheet from spreadsheet with one shot
#(temp) wks = gc.open("Where is the money Lebowski?").sheet1

#(temp) wks.update_acell('B2', "it's down there somewhere, let me take another look.")

# Fetch a cell range
#(temp) cell_list = wks.range('A1:B7')
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
gc = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
#(temp) sheet = client.open("Survey_Project_Responses").sheet1

sh = gc.create('This is just a test')

# But that new spreadsheet will be visible only to your script's account.
# To be able to access newly created spreadsheet you *must* share it
# with your email. Which brings us to sharing a spreadsheet 

sh.share('tthale02@gmail.com', perm_type='user', role='writer')