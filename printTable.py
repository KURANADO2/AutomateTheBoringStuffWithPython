#! python3
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable():
    s = ''
    for i in range(len(tableData)):
        max = -1
        for j in range(len(tableData[0])):
            if max < len(tableData[i][j]):
                max = len(tableData[i][j])
        print()
        s += str(max)

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(int(s[j])) + ' ', end='')
        print()


printTable()