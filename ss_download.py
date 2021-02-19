import ezsheets
from datetime import datetime

ss = ezsheets.createSpreadsheet('Delete this later -- ' + str(datetime.now()))
print(ss.title)

ss.downloadAsExcel() # Downloads the spreadsheet as an Excel file.
ss.downloadAsODS() # Downloads the spreadsheet as an OpenOffice file.
ss.downloadAsCSV() # Only downloads the first sheet as a CSV file.
ss.downloadAsTSV() # Only downloads the first sheet as a TSV file.
ss.downloadAsPDF() # Downloads the spreadsheet as a PDF.
ss.downloadAsHTML() # Downloads the spreadsheet as a ZIP of HTML files.

ss.delete(permanent=True)