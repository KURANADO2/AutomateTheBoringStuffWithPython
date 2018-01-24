import os
import re
import shutil
import random


def eliminateMissingNumber(folder):
    for root, dirs, files in os.walk():
        pass


def generateFile(folder):
    for fileNumber in range(25):
        if fileNumber >= 9:
            file = open(os.path.join(folder, 'spam0' + str(fileNumber + 1) + '.txt'), 'w')
        else:
            file = open(os.path.join(folder, 'spam00' + str(fileNumber + 1) + '.txt'), 'w')
        file.write(str(fileNumber + 1))
        file.close()


def randomDeleteFiles(folder):
    for fileNumber in range(6):
        randomNum = random.randint(1, 25)
        if len(str(randomNum)) == 1:
            os.unlink(os.path.join(folder, 'spam00' + str(randomNum) + '.txt'))
        else:
            os.unlink(os.path.join(folder, 'spam0' + str(randomNum) + '.txt'))


generateFile('E:\\Pictures\\Test')
randomDeleteFiles('E:\\Pictures\\Test')
