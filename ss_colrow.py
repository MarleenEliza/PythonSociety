import ezsheets
from datetime import datetime

print( ezsheets.convertAddress('A2') ) # Converts addresses...
print( ezsheets.convertAddress(1, 2) ) # ...and converts them back, too.
print( ezsheets.getColumnLetterOf(2) )
print( ezsheets.getColumnNumberOf('B') )
print( ezsheets.getColumnLetterOf(999) )
print( ezsheets.getColumnNumberOf('ZZZ') )

ss = ezsheets.upload('produceSales.xlsx')
sheet = ss[0]
sheet.getRow(1) # The first row is row 1, not row 0.

sheet.getRow(2)
columnOne = sheet.getColumn(1)
sheet.getColumn(1)
sheet.getColumn('A') # Same result as getColumn(1)
sheet.getRow(3)
sheet.updateRow(3, ['Pumpkin', '11.50', '20', '230'])
sheet.getRow(3)
columnOne = sheet.getColumn(1)
for i, value in enumerate(columnOne):
    columnOne[i] = value.upper()
sheet.updateColumn(1, columnOne) # Update the entire column in one request.

ss.downloadAsExcel() # Downloads the spreadsheet as an Excel file.