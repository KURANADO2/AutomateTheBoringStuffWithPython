import os
import csv

folder = 'D:\\Python'
os.makedirs(os.path.join(folder, 'headerRemoved'), exist_ok=True)
for fileName in os.listdir(folder):
    if not fileName.endswith('.csv'):
        continue
    print('Opening file ' + fileName + '...')
    file = open(os.path.join(folder, fileName))
    print('Reading file ' + fileName + '...')
    reader = csv.reader(file)
    print('Creating file ' + fileName + '...')
    newFile = open(os.path.join(folder, 'headerRemoved', fileName), 'w', newline='\n')
    writer = csv.writer(newFile)
    for row in reader:
        if reader.line_num == 1:
            continue
        writer.writerow(row)
    print('Write file ' + fileName + ' Done!')
    file.close()
    newFile.close()
