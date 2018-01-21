import os

for folderName, subFolders, fileNames in os.walk('D:\\Python\\Test'):
    # print('The current folder is ' + folderName)
    # for subFolderName in subFolders:
    #     print('The current subfolder is ' + subFolderName)

    for fileName in fileNames:
        print('The current filename is ' + fileName)