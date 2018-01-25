#! python3
import pprint
import openpyxl

countyData = {}
wb = openpyxl.load_workbook('D:\\Python\\censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

print('Writing file...')
file = open('D:\\Python\\census2010.py', 'w')
file.write('allData = ' + pprint.pformat(countyData))
file.close()
print('Write done!')
