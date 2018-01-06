# Google_Spreadsheet_Updater
A Python script that edits a spreadsheet from Google.

In order to be able to properly run this program you must have:
Rudimentary knowledge in Python
Basic knowledge of how to work the Command Console
A PC that is able to function correctly
Internet
The necessary plugins installed:
- Python (Preferably Version 2.7.14)
- Any other libraries can be installed by inputting [pip install (Library)]. The Command Console will say what Library needs to be installed.
- If necessary the Library can be updated by running [pip install (Library) update]
- The content I provide/describe (if you aren’t braindead this should be obvious)

This program makes use of the Google Drive API by creating and sharing a Google Spreadsheet, along with inputting information into the Spreadsheet.
It was written by me using Python version 2.7.14
This program probably works with versions Python 2.6+
There is no guarantee of the program working with versions lower than 2.6 or any 3.X versions.
To check what version of python you have installed onto your computer run [python -V] in the Command Console

In order for the program to work you must have a client_secrets.json file in the same directory that you put my program in. This is to bypass the OAuth2 security that Google uses.
In order to get a client_secrets.json file go to [https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html] And follow the steps that he specifies.
Even though the steps needed are a little bit different, they should be similar enough so that you can properly find your client secrets.
Once you find them, download them to the same directory the program is.
(Note: If the file isn’t called client_secrets, please rename it to that)

It works using the Command Console found in Windows and Linux PCs (Sorry Mac Users!) with the [sys.argv] function. In order to make it work type in [python] [Document Name.py] 
[The Spreadsheet Name] [The Worksheet Name] [General Content]. So, an working example would be [python fill_spreadsheet.py Hale_Spreadsheet First One To Be Here]. Here, [python] specifies to the console to read the program using python, [fill_spreadsheet.py] is the file that will be opened and ran, [Hale_Spreadsheet] is the spreadsheet that will be opened, [First] is the Worksheet that will be opened, 
and [One To Be Here] is what will be put into the spreadsheet.

Note that if a spreadsheet or a worksheet cannot be opened under that name, it will create one with that name instead and open it. 

Also, before running the program, please change the [ed] variable to your google account email that you want the program to share it to. The program will not work if you do not do this.
This can be done in an application known as Notepad++, a very basic coding program.
Go to https://notepad-plus-plus.org/ to download it. (It can also be done with Wordpad, but please don’t do that. No telling what harm it could do to the program)

The finished (well as close as possible to) version of my program is the fill_spreadsheet document. All others are either there for testing or earlier iterations of the program. 


