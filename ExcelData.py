#! python3
''' This is a short program to fetch certain data from an
Excel file and output it in a new Python file, which in turn
can then be analysed by itself.
'''

import openpyxl, pprint
print('Opening Excel workbook...')
wb = openpyxl.load_workbook('data.xlsx')
sheet = wb.get_sheet_by_name('PII')
data = {}

print('Reading rows in Excel file...')
for row in range(2, sheet.max_row + 1):
	department = sheet['B' + str(row)].value
	team = sheet['C' + str(row)].value
	amount = sheet['D' + str(row)].value

data.setdefault(department, {})
data[department].setdefault(team, {'contract':0, 'amount':0})
data[department][team]['contract'] += 1
data[department][team]['amount'] += int(amount)

print('Writing results to a new file...')
resultFile = open('output.py', 'w')
resultFile.write('allData = ' + pprint.pformat(data))
resultFile.close()
print('Operations are succesfully executed.')
