#! python3

import re
import os
import shutil

# 将sourceFolder下的指定扩展名文件扩展到destinationFolder下
def selectiveCopy(sourceFolder, destinationFolder):
    filePattern = re.compile(r'(.mp4)|(.jpg)|(.png)|(pdf)$')
    if not os.path.exists(destinationFolder):
        os.mkdir(destinationFolder)
    for root, dirs, files in os.walk(sourceFolder):
        # print('root: ' + root + '-----' + os.getcwd())
        for dir in dirs:
            # print('dir: ' + dir + '-----' + os.getcwd())
            pass
        for file in files:
            mo = filePattern.search(file)
            if mo is None:
                continue
            else:
                # print('file: ' + file + '-----' + os.getcwd())
                shutil.copy(os.path.join(root, file), destinationFolder)


selectiveCopy('E:\\Pictures', 'D:\\Pictures2')
