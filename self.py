import openpyxl


book = openpyxl.load_workbook("C:\\Users\\Anurag Goyal\\OneDrive\\Documents\\Book1.xlsx")

sheet = book.active

cell = sheet.cell(row=2,column=2)
print(cell.value)