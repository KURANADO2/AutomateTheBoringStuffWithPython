#! python3
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneNumRegex2 = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone num is 323-432-8342')
mo2 = phoneNumRegex2.search('My phone num is （323）-432-8342')
# 传入0和不传参数效果相同，都会返回整个匹配的文本
print(mo.groups())
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))