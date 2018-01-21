#! python3

import os

# 删除指定目录下大于100MB的文件
def delUnneedFile(root):
    for root, dirs, files in os.walk(root):
        for file in files:
            s = os.path.join(root, file)
            print(os.path.abspath(s) + '------' + str(os.path.getsize(s)/(1024 * 1024)))
            if os.path.getsize(s) / (1024 * 1024) > 100:
                os.unlink(s)


delUnneedFile('E:\\Pictures')