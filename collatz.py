def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1


while True:
    try:
        num = int(input('Enter number:'))
        break
    except ValueError:
        print('The value must be an integer!')
        continue
retValue = collatz(num)
print(retValue)
while retValue != 1:
    retValue = collatz(retValue)
    print(retValue)

