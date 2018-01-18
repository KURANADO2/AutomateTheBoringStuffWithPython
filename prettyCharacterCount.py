import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)

# 下面这条打印语句效果和上面的效果相同
print(pprint.pformat(count))