# 需求：
# 检查当前工作目录的所有文件名，寻找美国风格的日期
# 如果找到，将该文件改名，交换月份和日期的位置，使之成为欧洲风格
# 实现步骤：
# 1.创建一个正则表达式，可以识别美国风格日期的文本模式
# 2.调用os.listdir()，找出工作目录中的所有文件
# 3.循环遍历每个文件名，利用正则表达式检查其是否包含日期
# 4.如果其包含日期，用shutil.move()对该文件改名

import re
import shutil
import os

dataPattern = re.compile(r"""
^(.*?)
([01]?\d)-
([0123]?\d)-
((19|20)\d\d)
(.*?)$
""", re.VERBOSE)

os.chdir('D:\\Python\\OS')

for amerFileName in os.listdir('.'):
    mo = dataPattern.search(amerFileName)
    if mo is None:
        continue
    else:
        beforePart = mo.group(1)
        monthPart = mo.group(2)
        dayPart = mo.group(3)
        yearPart = mo.group(4)
        afterPart = mo.group(6)
        euroFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
        print('Renameing %s to %s' %(amerFileName, euroFileName))
        shutil.move(amerFileName, euroFileName)

