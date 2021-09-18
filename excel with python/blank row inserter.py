import openpyxl,sys

if len(sys.argv) > 1:
    row_start = int(sys.argv[1])
    num_to_insert = int(sys.argv[2])
    filename = sys.argv[3]

wb = openpyxl.load_workbook(filename)
sheet = wb.active
sheet.insert_rows(3,2)

wb.save('new_excel.xlsx')