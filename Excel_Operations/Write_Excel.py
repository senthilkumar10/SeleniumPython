import openpyxl

path = "./TC002.xlsx"

Work_Book = openpyxl.load_workbook(path)

Sheet = Work_Book.get_sheet_by_name("Sheet1")


for r in range(1,5):
    for c in range(1,4):
        Sheet.cell(r,c).value = "Welcome"


Work_Book.save(path)