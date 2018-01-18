spam = ['apples', 'bannas', 'tofu', 'cats']
spam2 = ['apples']


def comma_code(list_parameter):
    print('\'', end='')
    length = len(list_parameter)
    if length == 1:
        print(list_parameter[0] + '\'')
        return
    for i in range(length):
        if i != length - 1:
            print(list_parameter[i] + ',', end='')
        else:
            print('and ' + list_parameter[i] + '\'')


comma_code(spam2)