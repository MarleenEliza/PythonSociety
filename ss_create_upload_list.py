import ezsheets
from datetime import datetime

ss_new = ezsheets.createSpreadsheet('Delete this later -- ' + str(datetime.now()))
# Cannot repeatedly create new spreadsheets with the same name

ss_up = ezsheets.upload('upload_my_spreadsheet.xlsx')

ezsheets.listSpreadsheets()

print(ss_new.title)

print(ss_up.title)

d = ezsheets.listSpreadsheets()

for key in d:
    print(d[key])



# Attributes
print(ss_new.title)
print(ss_new.spreadsheetId)
print(ss_new.url)
print(ss_new.sheetTitles)
print(ss_new.sheets)

# Sheets can be accessed by index or title.
ss_new[0]
ss_new['Sheet1']
del ss_new[0]                 # Delete the first Sheet object in this Spreadsheet.
print(ss_new.sheetTitles)     # The "Students" Sheet object has been deleted:

ss_new.refresh()