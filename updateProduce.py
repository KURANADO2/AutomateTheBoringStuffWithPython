#! python3
import openpyxl
import os

PRICE_UPDATE = {
    'Garlic': 3.07,
    'Celery': 1.19,
    'Lemon': 1.27
}
os.chdir('D:\\Python')
wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb['Sheet']
for row in range(2, sheet.max_row + 1):
    proName = sheet['A' + str(row)].value
    if proName in PRICE_UPDATE.keys():
        sheet['B' + str(row)].value = PRICE_UPDATE[proName]

wb.save('produceSales_copy.xlsx')