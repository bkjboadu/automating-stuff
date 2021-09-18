import openpyxl as pyxl
prices = {'Garlic':2.5,'Celery':4,'Lemons':10}

wb = pyxl.load_workbook('produceSales.xlsx')
active = wb.active

for row in range(2,active.max_row + 1):
    if active['A' + str(row)].value == 'Garlic':
        active['B' + str(row)].value = prices['Garlic']
    elif active['A' + str(row)].value == 'Celery':
        active['B' + str(row)].value = prices['Celery']
    elif active['A' + str(row)].value == prices['Lemons']:
        active['B' + str(row)].value = prices['Lemons']
    else:
        pass

wb.save('new_p.xlsx')